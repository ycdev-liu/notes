
let str ="str"
// str =0  错误 类型约束

// 类型注解
let str1: string
str ="abc"


//  类型断言
// 手动确定设置类型
 let numArr =[1,2,3]
 const result = numArr.find(item => item>2)
//  result *5 报错
let numArr1 =[1,2,3]
const result1 = numArr1.find(item => item>2) as number
result1 *5


// 基础类型和联合类型

let v1:string = 'abc'
let v2:number =10
let v3:boolean = true
let nu: null = null
let un:undefined = undefined

let v4: string| null = null // 限制类型
let v5:1|2|3 =2 //限制数据

// 数组元组与枚举

let arr: number[] =[1,2,3]

let arr1: Array<string> =['a','b',"c"]


// 元组
// 限制了长度 限制了类型
let t1:[number,string,number?]=[1,"a",2]


enum MyEnum{
    A,
    B,
    C
}
MyEnum.A
MyEnum[0]

// void 只能了分配 undefined



function MyFn(a:number ,b:string):string{

    return a+b
}


function MyFn1(a:number ,b?:string,...rest:number[]):void{



}

const f = MyFn1(10,"abc",1,2,3,5)


// 接口

interface Obj{
    name:string,
    age:number
}
// 防止定义属性出现偏差

const obj:Obj ={
    name :"a",
    age:10

}

// 类型别名

type MyUserName = string|number

let a : string| number =10

let b: MyUserName =10

// 范性

function MyFn4<T>(a:T,b:T): T[]{
    return [a,b]


}


MyFn4<number>(1,2)
MyFn4<string>('a','b')


// 进阶
// 类型重载

function hello(name:string):string
function hello(age:number):string
function hello(value:string|number):string{

    if (typeof value ==='string'){
        return 'my name is '+value
    }
    else if(typeof value ==='number'){
        return `my age is ${value}`
    }
    else {
        
        return "error value"
    }

}

hello(12)
hello("str")

// 接口继承
 
interface Parent{
    prop1:string
    prop2:number
}

interface Child extends Parent{
    prop3:string
}
// 实现接口功能
const myObj : Child ={
    prop1:'',
    prop2:1,
    prop3:''
}

// 类


class Article {
    public title:string 
    content:string
    aa?:string
    bb =100

    private tempData? : string
    protected  InnerData?: string

    static  readonly author :string ="liu"
    private static reference :string




    constructor(title:string ,content :string)
    {
        this.title =title
        this.content = content
        // Article.author="wang" 报错 只读属性

    }
}


const cal1  = new Article("liu","content")

Article.author="liu"
class B extends Article{

    constructor(title:string,content:string){
        super(title,content)
        this.InnerData


    }
}


// 存取器
class User{
    private _password: string=''
    get password(): string{
        return "*******"
    }
    set password(newPass:string){
        this._password = newPass
    }

}
const u = new User()

// 抽象类

abstract class Animal{
    abstract name:string
    abstract maskSound():void

    move():void{
        console.log("移动")
    }
}

class Cat extends Animal{
    name: string ="cat"
    maskSound(): void {
        
    }
}

// 单继承多实现
interface Animal1{
    name:string
    get sound():string
    makeSound():void

}

interface B{
    age :number
}

class Dog implements Animal1, B{
    name:string ="dog"
    get sound(){
        return ''
    }
    makeSound():void{


    }
    age: number=10
}


// 类的泛型
class Myclass <T>{
    public value:T

    constructor(value:T){
        this.value = value
    }
    do (input:T){
        console.log("处理数据",this.value)
        return input
    }
}
const myStr = new Myclass<string>("hello")
myStr.do("one")

const mynumber = new Myclass<number>(123)
mynumber.do(121)