# _*_ encoding:utf-8 _*_

#导入程序所需的库
import re
import requests

# #定义URl地址
#url = 'https://book.douban.com/'
#
# #伪装客户端浏览器信息，防止爬取失败
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
#
# #获取网页信息
# response = requests.get(url,headers=headers).text
# print(response)


#根据网页信息获取163音乐榜单的所有歌曲,通过Re正则表达式筛选想要的信息
#用到re.compile,re.sub,re.findall方法

html='''
<li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/34841771/?icn=index-latestbook-subject" title="欲望的旗帜">
                <img src="https://img9.doubanio.com/view/subject/s/public/s33586354.jpg" class="" alt="欲望的旗帜">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/34841771/?icn=index-latestbook-subject" title="欲望的旗帜">欲望的旗帜</a>
              </div>
              <div class="author">
                格非
              </div>
              <div class="more-meta">
                <h4 class="title">
                  欲望的旗帜
                </h4>
                <p>
                  <span class="author">
                    格非
                  </span>
                  /
                  <span class="year">
                    2020-1
                  </span>
                  /
                  <span class="publisher">
                    浙江文艺出版社
                  </span>
                </p>
                <p class="abstract">
               </li>
'''
# conment = requests.get('https://book.douban.com/',headers=headers).text

parameter = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?publisher">(.*?)</span>.*?</li>',re.S)
result = re.findall(parameter,html)

for results in result:
    url,name,author,date,publisher = results
    author = re.sub('\s','',author)
    date = re.sub('\s','',date)
    publisher = re.sub('\s','',publisher)
    print(url,name,author,date,publisher)



