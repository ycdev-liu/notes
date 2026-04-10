import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Categorical
import numpy as np
import gym

# ===== 1. Actor-Critic 网络结构 =====
# PPO 通常采用 Actor-Critic 架构。Actor 负责输出动作概率（策略），Critic 负责评估当前状态的价值。
class ActorCritic(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        # 共享特征提取层：Actor 和 Critic 共享底层特征，可以加快训练并减少参数量
        self.shared = nn.Sequential(
            nn.Linear(state_dim, 64),
            nn.Tanh()
        )
        # Actor 头部：输出每个离散动作的未归一化概率（logits）
        self.actor = nn.Linear(64, action_dim)
        # Critic 头部：输出当前状态的状态价值 V(s)
        self.critic = nn.Linear(64, 1)

    def forward(self, x):
        x = self.shared(x)
        logits = self.actor(x)
        value = self.critic(x)
        return logits, value


# ===== 2. 广义优势估计 (GAE, Generalized Advantage Estimation) =====
# GAE 用于在“低方差（偏向直接用价值网络）”和“低偏差（偏向使用实际多步回报）”之间做平滑过渡。
def compute_gae(rewards, values, dones, gamma=0.99, lam=0.95):
    advantages = []
    gae = 0
    # 补充最后一个状态的价值为 0（用于 bootstrap），方便倒序计算
    values = values + [0]  

    # 逆序遍历时间步，计算优势函数 (Advantage)
    for t in reversed(range(len(rewards))):
        # 计算 TD Error (时序差分误差): r + gamma * V(s') - V(s)
        # 如果 done=True (游戏结束)，则没有下一个状态的价值，(1 - dones[t]) 会将其置为 0
        delta = rewards[t] + gamma * values[t+1] * (1 - dones[t]) - values[t]
        
        # 累加 GAE: A_t = delta_t + gamma * lambda * A_{t+1}
        gae = delta + gamma * lam * (1 - dones[t]) * gae
        # 每次插入到列表头部，保证最终的时间顺序是正向的
        advantages.insert(0, gae)

    return advantages


# ===== 3. PPO 核心更新逻辑 =====
def ppo_update(model, optimizer, states, actions, old_log_probs,
               returns, advantages, epochs=10, batch_size=64, eps=0.2):

    # 将收集到的经验列表转换为 PyTorch 张量
    states = torch.tensor(states, dtype=torch.float32)
    actions = torch.tensor(actions)
    old_log_probs = torch.tensor(old_log_probs, dtype=torch.float32)
    returns = torch.tensor(returns, dtype=torch.float32)
    advantages = torch.tensor(advantages, dtype=torch.float32)

    # ✅ 标准化 Advantage（非常关键的工程技巧）
    # 这能让训练更稳定，使得不同批次的数据在一个相近的尺度上更新梯度
    advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)

    dataset_size = states.size(0)

    # PPO 允许我们复用收集到的这一批数据进行多次更新 (epochs)
    for _ in range(epochs):
        # 打乱数据索引，准备进行小批量 (mini-batch) 训练
        indices = np.random.permutation(dataset_size)

        for start in range(0, dataset_size, batch_size):
            end = start + batch_size
            batch_idx = indices[start:end]

            # 获取当前 mini-batch 的数据
            s = states[batch_idx]
            a = actions[batch_idx]
            old_lp = old_log_probs[batch_idx]
            ret = returns[batch_idx]
            adv = advantages[batch_idx]

            # 用当前网络重新评估这些状态，得到最新的 logits 和 价值
            logits, values = model(s)
            dist = Categorical(logits=logits)

            # 计算当前策略下，采取这些动作的新对数概率和信息熵
            new_log_probs = dist.log_prob(a)
            entropy = dist.entropy().mean()

            # ===== PPO 核心截断机制 (Clipped Objective) =====
            # 1. 计算重要性采样比率 ratio = pi_theta(a|s) / pi_theta_old(a|s)
            # 由于使用的是 log 概率，相减再 exp 就等于概率相除
            ratio = torch.exp(new_log_probs - old_lp)

            # 2. 计算代理目标 (Surrogate Objective) 的两部分
            surr1 = ratio * adv
            # 限制 ratio 在 [1-eps, 1+eps] 之间。如果动作优势大，且更新步伐过大，将被截断
            surr2 = torch.clamp(ratio, 1-eps, 1+eps) * adv

            # 3. Actor Loss: 取两者的较小值（悲观估计），并加负号变为最小化问题
            actor_loss = -torch.min(surr1, surr2).mean()

            # ===== Critic 损失 =====
            # 价值网络的损失是简单的均方误差 (MSE)，目标是预测真实的 Return
            critic_loss = (ret - values.squeeze()).pow(2).mean()

            # ===== 总损失 =====
            # 减去 entropy 是为了作为正则项，鼓励模型输出更均匀的概率，增加探索 (Exploration)
            loss = actor_loss + 0.5 * critic_loss - 0.01 * entropy

            # 梯度清零，反向传播
            optimizer.zero_grad()
            loss.backward()

            # ✅ 防梯度爆炸：限制梯度的最大范数
            torch.nn.utils.clip_grad_norm_(model.parameters(), 0.5)

            # 更新网络参数
            optimizer.step()


# ===== 4. 训练主循环 =====
def train():
    # 创建经典控制任务环境
    env = gym.make("CartPole-v1")

    state_dim = env.observation_space.shape[0] # 状态维度 (4)
    action_dim = env.action_space.n            # 动作维度 (2：向左或向右)

    # 初始化模型和优化器
    model = ActorCritic(state_dim, action_dim)
    optimizer = optim.Adam(model.parameters(), lr=3e-4)

    max_episodes = 500
    rollout_steps = 2048 # 每次更新前收集的步数（PPO 是 On-policy 算法，收集一段数据更新一次）
     # PPO 的训练流程分为三个阶段：
     # 1. 收集经验 (Rollout)：与环境交互，收集状态、动作、奖励等数据
     # 2. 计算优势和目标回报：使用 GAE 计算 Advantage，并计算目标回报 Return
     # 3. 更新网络参数：使用 PPO 的核心更新逻辑，进行多次迭代更新网络参数
     # 通过多次迭代更新同一批数据，PPO 能更充分地利用收集到的经验，提高样本效率，同时通过截断机制保持训练稳定。
    for episode in range(max_episodes):
        # 用于存储每一步经验的列表
        states, actions, rewards = [], [], []
        dones, log_probs, values = [], [], []

        state = env.reset()[0]

        # 阶段一：收集经验 (Rollout)
        for _ in range(rollout_steps):
            state_tensor = torch.tensor(state, dtype=torch.float32)

            # 网络前向传播，不计算梯度 (在 PPO 更新时才计算梯度)
            logits, value = model(state_tensor)
            dist = Categorical(logits=logits)

            # 根据概率分布采样动作
            action = dist.sample()

            # 与环境交互
            next_state, reward, done, _, _ = env.step(action.item())

            # 记录数据
            states.append(state)
            actions.append(action.item())
            rewards.append(reward)
            # done 是一个布尔值，表示游戏是否结束。PPO 需要知道哪些状态是 episode 结束的，以正确计算 GAE 和目标回报
            dones.append(done)
            log_probs.append(dist.log_prob(action).item()) # 记录旧策略的概率
            values.append(value.item())

            state = next_state

            # 如果游戏提前结束，重置环境
            if done:
                state = env.reset()[0]

        # 阶段二：计算优势和目标回报
        # GAE 计算 Advantage
        advantages = compute_gae(rewards, values, dones)
        # 目标回报 Return = Advantage + Value (由 GAE 公式推导而来)
        returns = [a + v for a, v in zip(advantages, values)]

        # 阶段三：使用收集到的数据更新网络参数
        ppo_update(model, optimizer, states, actions, log_probs, returns, advantages)

        # 打印日志
        if episode % 10 == 0:
            print(f"Episode {episode} done")


if __name__ == "__main__":
    train()