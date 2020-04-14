# _*_ coding:utf-8 _*_
# encoding:utf-8

#引入库
import requests
from lxml import etree

#定义URL变量
firstlink = "https://book.douban.com/subject/30172069/comments/hot?p=6"

#定义函数
def stepa (firstlink):
    response = requests.get(url=firstlink)
    wl_data = response.text
    html = etree.HTML(wl_data)
    a = html.xpath('//*[@id="comments"]//div[2]/p/span/text()')
    print(a)


stepa (firstlink)