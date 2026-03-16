

// import http from 'http';
// const server = http.createServer((request,response)=>{
//     console.log("有人敲门了")
//     response.writeHead(200,{'Content-Type':"text/plain;charset=utf-8"});

//     const url =request.url


// if (url === '/') {
//         response.end('<h1>欢迎来到首页 🏠</h1>');
//     } else if (url === '/about') {
//         response.end('<h1>关于我：我是 JS 学习者 👨‍💻</h1>');
//     } else if (url === '/data') {
//         // 还记得我们要返回 JSON 数据吗？
//         const data = { name: "Tony", level: 99 };
//         response.end(JSON.stringify(data));}
//     else if(url === "/time") {
//         const time = new Date().toLocaleString()
//         response.end(`现在的时间是 ${time}`)


//     }
//     else {
//         // 404 处理
//         response.end('<h1 style="color:red">404 - 找不到页面 😭</h1>');
//     }

//     // response.end("你好,这是我第一个node.js")
// }
    
// )
// const PORT = 3000;
// server.listen(PORT, ()=>{console.log(`🚀 服务器启动成功！正在监听 http://localhost:${PORT}`);});


import express from 'express';

const app = express()

const PORT = 3000;

app.get('/',(req,res) =>{
    res.send('<h1>欢迎来到 Express 首页 🏠</h1>');
});
app.get('/about', (req, res) => {
    res.send('<h1>关于我：Express 真香 🚀</h1>');
});

// 路由 3：返回数据 (自动变 JSON)
app.get('/data', (req, res) => {
    const data = { name: "Tony", level: 99 };
    // res.json() 专门用来返回数据，比 JSON.stringify() 更专业
    res.json(data); 
});

// 路由 4：时间
app.get('/time', (req, res) => {
    const time = new Date().toLocaleString();
    res.send(`<h2>现在的系统时间是: ${time}</h2>`);
});

app.get('/hello/:name',(req,res)=>{
    const {name} = req.params;
    res.send(`<h1>你好啊，${name} 欢迎光临！</h1>`);
})


app.post('/login',(req,res)=>{
    const {username,password} = req.body;
    
    console.log(`收到登录请求: 用户名=${username},密码=${password}`);

    if (username === 'admin' && password==='123456'){
        res.json({success:true,message:"登录成功 欢迎回来，管理员"});
    }
    else {
        // 401 代表 "未授权"
        res.status(401).json({ success: false, message: "用户名或密码错误！" });
    }

})

app.listen(PORT, () => {
    console.log(`🚀 Express 服务器启动成功！访问 http://localhost:${PORT}`);
});