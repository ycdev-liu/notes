

function createCounter(){

    let count =0;
    // return function() {
    //     count = count +1;
    //     return count;
    // }

    function increment(){

        count = count+1;
        return count;
    }
    function decrement(){

        count =count -1;
        return count;
    }

    return {
        increment: increment,
        decrement: decrement
    }
}

const myCounter = createCounter();


// console.log(myCounter());
// console.log(myCounter());



console.log(myCounter.increment());
console.log(myCounter.increment());
console.log(myCounter.decrement());




let color ="红色（全局）"

function outer() {
    let color ="蓝色（外部函数）"

    function inner() {
        // let color ="绿色 （内部函数）"
        console.log("inner 里面可以看到是",color)
    }

    inner();
    console.log("couter 里面看到什么",color)


}

outer();
console.log("全局看到的是",color)



let number = 100

function showNumber() {
    console.log(number)
}

function magic(){

    let number =42;
    showNumber();

}

// showNUmber() 是在全局调用的 所有它的作用域在全局 

magic();
// 100


function initConfig(userConfig){


    const defaultConfig ={
        theme :"light",
        language :"en",
        notifications: true
    };
    // const{language:language}=userConfig;
    // console.log(language)



    const finalConfig={
        ... defaultConfig,
        // language:language
        ... userConfig
    };


    const {theme,language} =finalConfig;

    console.log(`主题：${theme} 语言${language}`);

    return finalConfig;



}


const project= initConfig({language:"zh-CN"})

console.log(project
)

const prices = [100,200,300]

const discountedPrices =prices.map(item=>item*0.9)

console.log(discountedPrices)



const products=[
    {name:"苹果",prices:5},
    {name:"电脑",prices:8000},
    {name:"手机",prices:4000},
    {name:"面包",prices:10}

]

const cheapProducts=products.filter(item=>item.prices<100)

console.log(cheapProducts)


const users =[
    {id:101,name:"Alice"},
    {id:102,name:"Bob"},
    {id:103,name:"Charlie"},
    {id:104,name:"David"}
]


const targetUser =users.find(item=>item.name ==="Charlie");

console.log(targetUser)


// 1. 创建一个 Promise (给厨师下达任务)
// const cookDinner = new Promise((resolve, reject) => {
//     console.log("👨‍🍳 厨师：开始做饭...");
    
//     // 模拟耗时操作 (2秒后完成)
//     setTimeout(() => {
//         const isSuccess = true; // 假设做饭成功

//         if (isSuccess) {
//             // ✅ 成功了！调用 resolve，把结果交出去
//             resolve("🍜 拉面做好了！"); 
//         } else {
//             // ❌ 失败了！调用 reject，把错误交出去
//             reject("🔥 厨房着火了！");
//         }
//     }, 2000); // 2000 毫秒 = 2 秒
// });

// // 2. 拿到取餐号后，我们要规定“饭好了以后做什么”
// console.log("🧑 我：在等饭，先玩会儿手机...");

// cookDinner
//     .then((result) => {
//         // 只有当 resolve 被调用时，才会进这里
//         console.log("😋 终于吃上了:", result);
//     })
//     .catch((error) => {
//         // 只有当 reject 被调用时，才会进这里
//         console.log("😭 悲剧发生:", error);
//     });

// console.log("📱 我：继续刷视频...");

// async function loginUser() {
//     return new Promise(  setTimeout(() => {
//         const isSuccess = true; // 假设做饭成功

//         if (isSuccess) {
//             // ✅ 成功了！调用 resolve，把结果交出去
//             resolve("🍜 拉面做好了！"); 
//         } else {
//             // ❌ 失败了！调用 reject，把错误交出去
//             reject("🔥 厨房着火了！");
//         }
//     }, 2000)// 2000 毫秒 = 2 秒
//     );
// }


function loginUser(){
    
    return new Promise((resolve,reject)=>
    {
        setTimeout(
            ()=>{
                const isSuccess = false;
                if (isSuccess){
                    resolve("成功");
                }
                else{
                    reject("登录失败");
                }
            },1000
        );

    });
}

async function startLogin(){

    console.log("开始登陆");


    try{
        const  result = await loginUser();
        console.log("成功",result)
    }
    catch (error){
        console.log("出错了", error)
    }
    console.log("流程结束")

}


// startLogin()


async function getCatFact() {

    console.log("联系猫咪星球...")

    try{

        const response = await fetch("https://catfact.ninja.fact");

        const data = await response.json();

        console.log("猫咪知识：",data.fact);
    }
    catch(error){
        console.log("无法连接猫咪星球",error);
    }
}

// getCatFact()



class BankAccount{

    constructor(owner,balance){
        this.owner = owner;
        this.balance = balance
    }

    deposit(amount) {
        this.balance +=amount
        console.log(`${this.owner}存入${amount}元,当前金额为${this.balance}`)

    }

    withdraw(amount){
        if(this.balance<amount){
            console.log(`余额不足`)
        }
        else{
            this.balance -= amount

            console.log(`你的剩余金额为${this.balance}`)

        }

    }


}
const banksatr = new BankAccount("张三",1000);
banksatr.owner
banksatr.balance
banksatr.deposit(100)
banksatr.withdraw(1000)



class VIPAmount extends BankAccount{
    addInterest(){
        const interest = this.balance*0.05;
        this.balance +=interest;
        console.log(`尊贵的vip用户${this.owner},您获得的利息${interest}`)

    }
    transfer(targetAccount,amount){
        console.log(`开始向${targetAccount.owner}转账`)
        this.withdraw(amount);
        targetAccount.deposit(amount);
    }
}

const liubei = new VIPAmount("liu",1000)
const zhangfei = new VIPAmount("zhang",100)

liubei.transfer(zhangfei,100)
console.log(liubei)
console.log(zhangfei)


const serverConfig = {
    timeout: 0,          // 0 是有效设置，代表不超时
    title: "",           // 空字符串，需要用默认标题 "未命名"
    details: null        // 彻底没了
};



function processConfig(config){

    const finalTimeout = config.timeout??3000;

    const finalTitle = config.title || "未命名";

    const version = config?.details?.version;
    console.log(`超时:${finalTimeout},标题${finalTimeout},版本${version}`)


}

processConfig(serverConfig)

const age = 20;

const status = age >= 18 ?"成年人":"未成年人"
console.log(status)

// function calculateTotal(level,...prices){

//     const goodTotal =prices.reduce((a,b)=>a+b,0);
//     // let shippingCost=0

//     // if (level === "VIP")
//     // {
//     // shippingCost=0
//     // }
//     // else
//     // {
//     //  shippingCost= goodTotal >= 200? 0 : 20;
//     // }


//     const shippingCost=(level==="VIP"||goodTotal>=200) ?0:20;

//     console.log(`用户等级${level}用户消费${goodTotal}运费${shippingCost}`)
//     return goodTotal + shippingCost;
    
// }


// calculateTotal("Normal",100,50)
// calculateTotal("Normal",100,200)
// calculateTotal("VIP",10,20)


import { calculateTotal,shopName } from "./test1.js";

console.log(`欢迎光临 ${shopName}!`);

const result = calculateTotal("Normal", 100, 50);
console.log("您的账单:", result)


import fs from 'fs/promises';

const FILE_NAME = "count.txt"

async function updateCounter() {

    let currentCount = 0;

    try{

        const content = await fs.readFile(FILE_NAME,"utf-8");
        currentCount=Number(content);

    } catch(error){
        console.log("第一次运行")
        currentCount =0;

    }
    currentCount +=1;
    await fs.writeFile(FILE_NAME,String(currentCount));
    
    console.log('这是第${currentCount}此运行程序')


}
updateCounter()