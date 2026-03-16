# 学习httpx库的使用
import httpx



"""
用例 1：GET 请求（查询天气）

场景：获取东京天气，不需要发送数据，只是查询。

请求行
GET /weather?city=Tokyo HTTP/1.1
请求头
Host: api.example.com
User-Agent: MyWeatherApp/1.0
Accept: application/json
请求体
（空）
说明：
GET 请求通常没有请求体，参数通过 URL query 传递。
请求头告诉服务器你希望返回 JSON，并标明客户端信息。
用例 2：POST 请求（用户登录）
场景：提交用户名和密码，服务器返回登录结果。
请求行
POST /api/login HTTP/1.1
请求头
Host: api.example.com
Content-Type: application/json
Accept: application/json
User-Agent: MyApp/2.0
请求体
{
  "username": "tom",
  "password": "123456"
}
说明：
POST 请求通常有请求体，传递敏感或结构化数据。
Content-Type: application/json 表示请求体是 JSON。
用例 3：PUT 请求（更新用户信息）
场景：修改用户昵称和邮箱。
请求行
PUT /api/users/1 HTTP/1.1
请求头
Host: api.example.com
Authorization: Bearer eyJhbGciOiJI...
Content-Type: application/json
Accept: application/json
User-Agent: MyApp/2.0
请求体
{
  "nickname": "Tommy",
  "email": "tommy@example.com"
}
说明：
PUT 请求用于替换资源或更新资源。
Authorization 提供用户身份认证。
用例 4：DELETE 请求（删除文章）
场景：删除 ID 为 101 的文章。
请求行
DELETE /api/articles/101 HTTP/1.1
请求头
Host: api.example.com
Authorization: Bearer eyJhbGciOiJI...
User-Agent: MyApp/2.0
Accept: application/json
请求体
（空）
说明：
DELETE 请求一般不需要请求体，只需要在 URL 中指定资源。
身份认证通常通过请求头完成。
总结
方法	请求体	常用请求头	用途
GET	空	Accept, User-Agent	获取数据
POST	有	Content-Type, Accept	提交数据
PUT	有	Content-Type, Authorization	更新数据
DELETE	空	Authorization, Accept	删除数据

"""




# httpx库提供了一个简单的API来发送HTTP请求，并且支持异步请求和并发请求。
# httpx.get()
# httpx.post()
# httpx.put()
# httpx.delete()


# 发送GET请求
response = httpx.get('https://httpbin.org/get')
print(response.status_code)
print(response.json())

# 发送POST请求
response = httpx.post('https://httpbin.org/post', data={'key': 'value'})
print(response.status_code)
print(response.json())

# 发送PUT请求
response = httpx.put('https://httpbin.org/put', data={'key': 'value'})
print(response.status_code)
print(response.json())

# 发送DELETE请求
response = httpx.delete('https://httpbin.org/delete')
print(response.status_code)
print(response.json())


# 发送带有自定义头部的请求
headers = {'User-Agent': 'httpx-test/1.0'}
response = httpx.get('https://httpbin.org/headers', headers=headers)
print(response.status_code)

# URL参数
params = {'search': 'httpx'}
response = httpx.get('https://httpbin.org/get', params=params)
print(response.status_code)
print(response.json())

# Client对象的使用
with httpx.Client() as client:
    response = client.get('https://httpbin.org/get')
    print(response.status_code)
    print(response.json())

# 超时连接
try:
    response = httpx.get('https://httpbin.org/delay/5', timeout=2.0)
except httpx.TimeoutException:
    print("请求超时")

# 异步请求
import asyncio
async def fetch():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://httpbin.org/get')
        print(response.status_code)
        print(response.json())
asyncio.run(fetch())

# 并发请求
import httpx
import asyncio

urls = [
    "https://httpbin.org/get",
    "https://httpbin.org/ip",
    "https://httpbin.org/user-agent"
]

async def fetch(url, client):
    r = await client.get(url)
    return r.status_code

async def main():
    async with httpx.AsyncClient() as client:
        tasks = [fetch(url, client) for url in urls]
        results = await asyncio.gather(*tasks)
        print(results)

asyncio.run(main())