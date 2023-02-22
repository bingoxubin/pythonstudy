# 爬虫
# 请求网站并提取数据的自动化程序
# 1、发起请求：通过http库目标站点发起请求，即发送一个request，请求可以包含额外的headers等信息，等待服务器响应
# 2、获取响应内容：如果服务器能够正常响应，会得到response，response的内容便是所要获取的页面内容，类型可能有html，json字符串，二进制数据如图片，视频等类型
# 3、解析内容：得到的内容可能是html，可以用正则表达式，网页解析库进行解析，可能是json，可以直接转为json对象解析，可能是二进制数据，可以做保存或者进一步处理
# 4、保存数据：保存形式多样，可以存为文本，也可以保存至数据库，或者保存特定格式的文件
# https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png
import requests

url = "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40'}
response = requests.get(url=url, headers=headers)  # 发送网络请求（get,post),模仿了浏览器的请求
print(response.content)  # 以二进制的形式返回内容，推荐
# print(response.text)  # 以文本的形式返回内容

# 保存内容
# file = open('baidu.png', 'wb')
# file.write(response.content)
# file.close()

# 自动关闭
with open('baidu.png', 'wb') as file:
    file.write(response.content)

# 请求request
'''
request是请求，在浏览器输入地址，回车就是一个请求
请求方式：主要有post，get两种，另外还有HEAD、PUT、DELETE、OPTIONS等
请求的URL：URL全称统一资源定位符，如一个网页的文档，一张图片，一个视频等都可以用URL来确定
请求头：包含请求时的头部信息，如User-Agent、host、Cookies等信息【post，登陆的时候】
'''
# 响应response
'''
response是响应，服务器根据请求，返回数据到浏览器显示，就是一个响应
响应状态：有多种响应状态，如200代表成功、301跳转、404找不到页面、502服务器错误等
响应头：如内容类型、内容长度、服务器信息、设置Cookie等
响应体：最主要的部分，包含了请求资源的内容，如网页HTML、图片二进制数据等
'''

# 案例，爬取妹子图网页上的图片
from lxml import etree
import requests

base_url = 'https://www.mzitu.com/jiepai/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40'}
response = requests.get(url=base_url, headers=headers)
print(response.text)
# 使用xpath解析数据
html = etree.HTML(response.text)
ul_list = html.xpath('//*[@id="comments"]/ul/li')
print(ul_list)

num = 0
for li in ul_list:
    num += 1
    img_url = li.xpath('./div/p/img/@data-original')[0]
    print(img_url)
    # 发送请求下载图片
    img_response = requests.get(url=img_url, headers=headers)
    with open('./source/{}.jpg'.format(num), 'wb') as file:
        file.write(img_response.content)
