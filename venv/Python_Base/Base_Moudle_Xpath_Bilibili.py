from lxml import etree
import requests
from bs4 import BeautifulSoup as bs

url = 'https://search.bilibili.com/all?keyword=python&from_source=banner_search&spm_id_from=333.334.b_62616e6e65725f6c696e6b.1'

response = requests.get(url).text
#
print(response)

wb_data = etree.HTML(response)
print(wb_data)
#
# result = wb_data.xpath('//*[@id="all-list"]/div[1]/div[2]/ul[2]/li[1]/a/@href')

# print(result)

# html = '''
# <a title="python教程2019版 6小时完全入门 并且达到能开发网站的能力 目前最好的python教程 （含中文翻译）" href="//www.bilibili.com/video/BV14J411U7hj?from=search&amp;seid=12593580953043186023" target="_blank" class="title"><em class="keyword">python</em>教程2019版 6小时完全入门 并且达到能开发网站的能力 目前最好的<em class="keyword">python</em>教程 （含中文翻译）</a>
# '''

soup = bs(response,'response.parser')
# result = soup.find_all('a')
# print(result)
# print('##'*30)
for link in soup.find_all('a'):
    print(link.get('href'),link.get('title'))





