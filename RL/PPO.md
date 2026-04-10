# ppo算法

组成
1.策略网路
2.价值网络
3.数据采样 （rollout）
4.计算优势（GAE）
5.更新参数 （PPO核心）

### 核心代码

```
import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Categorical

# ===== 1. Actor-Critic 网络 =====
class ActorCritic(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.shared = nn.Sequential(
            nn.Linear(state_dim, 64),
            nn.Tanh()
        )
        self.actor = nn.Linear(64, action_dim)
        self.critic = nn.Linear(64, 1)

    def forward(self, x):
        x = self.shared(x)
        logits = self.actor(x)
        value = self.critic(x)
        return logits, value


# ===== 2. 计算优势（GAE）=====
def compute_gae(rewards, values, gamma=0.99, lam=0.95):
    advantages = []
    gae = 0
    for t in reversed(range(len(rewards))):
        delta = rewards[t] + gamma * values[t+1] - values[t]
        gae = delta + gamma * lam * gae
        advantages.insert(0, gae)
    return advantages


# ===== 3. PPO更新 =====
def ppo_update(model, optimizer, states, actions, old_log_probs, returns, advantages, eps=0.2):

    logits, values = model(states)
    dist = Categorical(logits=logits)
    new_log_probs = dist.log_prob(actions)

    # 🔥 核心：概率比
    ratio = torch.exp(new_log_probs - old_log_probs)

    # 🔥 clip
    surr1 = ratio * advantages
    surr2 = torch.clamp(ratio, 1-eps, 1+eps) * advantages

    actor_loss = -torch.min(surr1, surr2).mean()

    critic_loss = (returns - values.squeeze()).pow(2).mean()

    loss = actor_loss + 0.5 * critic_loss

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```
🧩 1. Actor-Critic 网络
👉 输出两样东西：
logits → 动作概率（Actor）
value → 状态值 V(s)（Critic）
| 模块     | 作用 |
| ------ | -- |
| Actor  | 决策 |
| Critic | 评价 |




PPO-Clip 版本
```
--- python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Categorical
import numpy as np
import gym

# ===== 1. Actor-Critic =====
class ActorCritic(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.shared = nn.Sequential(
            nn.Linear(state_dim, 64),
            nn.Tanh()
        )
        self.actor = nn.Linear(64, action_dim)
        self.critic = nn.Linear(64, 1)

    def forward(self, x):
        x = self.shared(x)
        logits = self.actor(x)
        value = self.critic(x)
        return logits, value


# ===== 2. GAE =====
def compute_gae(rewards, values, dones, gamma=0.99, lam=0.95):
    advantages = []
    gae = 0
    values = values + [0]  # bootstrap

    for t in reversed(range(len(rewards))):
        delta = rewards[t] + gamma * values[t+1] * (1 - dones[t]) - values[t]
        gae = delta + gamma * lam * (1 - dones[t]) * gae
        advantages.insert(0, gae)

    return advantages


# ===== 3. PPO更新 =====
def ppo_update(model, optimizer, states, actions, old_log_probs,
               returns, advantages, epochs=10, batch_size=64, eps=0.2):

    states = torch.tensor(states, dtype=torch.float32)
    actions = torch.tensor(actions)
    old_log_probs = torch.tensor(old_log_probs, dtype=torch.float32)
    returns = torch.tensor(returns, dtype=torch.float32)
    advantages = torch.tensor(advantages, dtype=torch.float32)

    # ✅ 标准化 advantage（关键）
    advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)

    dataset_size = states.size(0)

    for _ in range(epochs):
        indices = np.random.permutation(dataset_size)

        for start in range(0, dataset_size, batch_size):
            end = start + batch_size
            batch_idx = indices[start:end]

            s = states[batch_idx]
            a = actions[batch_idx]
            old_lp = old_log_probs[batch_idx]
            ret = returns[batch_idx]
            adv = advantages[batch_idx]

            logits, values = model(s)
            dist = Categorical(logits=logits)

            new_log_probs = dist.log_prob(a)
            entropy = dist.entropy().mean()

            # ===== PPO核心 =====
            ratio = torch.exp(new_log_probs - old_lp)

            surr1 = ratio * adv
            surr2 = torch.clamp(ratio, 1-eps, 1+eps) * adv

            actor_loss = -torch.min(surr1, surr2).mean()

            critic_loss = (ret - values.squeeze()).pow(2).mean()

            loss = actor_loss + 0.5 * critic_loss - 0.01 * entropy

            optimizer.zero_grad()
            loss.backward()

            # ✅ 防梯度爆炸
            torch.nn.utils.clip_grad_norm_(model.parameters(), 0.5)

            optimizer.step()


# ===== 4. 训练主循环 =====
def train():
    env = gym.make("CartPole-v1")

    state_dim = env.observation_space.shape[0]
    action_dim = env.action_space.n

    model = ActorCritic(state_dim, action_dim)
    optimizer = optim.Adam(model.parameters(), lr=3e-4)

    max_episodes = 500
    rollout_steps = 2048

    for episode in range(max_episodes):
        states, actions, rewards = [], [], []
        dones, log_probs, values = [], [], []

        state = env.reset()[0]

        for _ in range(rollout_steps):
            state_tensor = torch.tensor(state, dtype=torch.float32)

            logits, value = model(state_tensor)
            dist = Categorical(logits=logits)

            action = dist.sample()

            next_state, reward, done, _, _ = env.step(action.item())

            states.append(state)
            actions.append(action.item())
            rewards.append(reward)
            dones.append(done)
            log_probs.append(dist.log_prob(action).item())
            values.append(value.item())

            state = next_state

            if done:
                state = env.reset()[0]

        # ===== GAE =====
        advantages = compute_gae(rewards, values, dones)
        returns = [a + v for a, v in zip(advantages, values)]

        # ===== PPO更新 =====
        ppo_update(model, optimizer, states, actions, log_probs, returns, advantages)

        if episode % 10 == 0:
            print(f"Episode {episode} done")


if __name__ == "__main__":
    train()

```

# 