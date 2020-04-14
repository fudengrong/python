# _*_　coding:utf-8 _*_
# encoding:utf-8

import requests
from bs4 import BeautifulSoup

start = 0

for n in range(0,10):
    html = requests.get('https://movie.douban.com/top250?start='+str(start))
    start += 30
    soup = BeautifulSoup(html.text,'html.parser')
    for item in soup.find_all('div','info'):
        title = item.div.a.span.sting #获取标题
        #print(title)
        yearline = item.find('div','bd').p.contents[2].string#获取年份
        yearline = yearline.replace(' ','')#去掉这一行的空格
        yearline = yearline.replace('\n','')#去掉这一行的回车换行
        year = yearline[0,4]#只去年份的前4个字符
        print(title,'\t',year)
