
# 引用相关模块
import requests
from bs4 import BeautifulSoup

#请求网易新闻的URL，获取TExt文本
url = 'https://www.163.com/'
wbdata = requests.get(url).text


#对获取到的文本进行解析
soup = BeautifulSoup(wbdata,'lxml')

#从解析文件中通过CSS选择器（select）定位指定的元素，返回一个列表
news_titles = soup.select("div>nul>li>a")

#对返回的列表进行遍历
for n in news_titles:
    #提取标题和链接信息
    title = n.get_text()
    link = n.get("href")
    print(title,link)
    #data = {
    #    '标题':title,
    #    '连接':link
    #}

    #print(data)
