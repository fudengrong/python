import pandas as pd
import requests
from lxml import etree
import time


#循环构造网址
def format_url(base_url,pages = 10):
    urls = []
    for num in range(0,pages * 25,25):
        urls.append(base_url.format(num))
    return urls

#解析单个页面
def parse_page(url,headers):
    #创建一个存储结果的容器
    result = pd.DataFrame()
    html = requests.get(url,headers = headers)
    bs = etree.HTML(html.text)
    for i in bs.xpath('//tr[@class = "item"]'):
        #书籍中文名
        book_ch_name = i.xpath('td[2]/div[1]/a[1]/@title')[0]
        #评分
        score = i.xpath('td[2]/div[2]/span[2]')[0].text
        #书籍信息
        book_info = i.xpath('td[2]/p[@class = "pl"]')[0].text
        #评价数量由于数据不规整，这里用PYTHON字符串方法对数据进行了处理
        comment_num = i.xpath('td[2]/div[2]/span[3]')[0].text.replace(' ','').strip('(\n').strip('\n)')
        try:
            #后面有许多书籍没有一句话概括
            #一句话概括
            brief = i.xpath('td[2]/p[@class = "quote"]/span')[0].text
        except:
            brief = None
        #这里的cache是存储每一次循环的结果，然后通过下一步操作循环更新result里面的数据
        cache = pd.DataFrame({'中文名':[book_ch_name],'评分':[score],\
                              '书籍信息':[book_info],'评价数量':[comment_num],'一句话概括':[brief]})
        #把新循环中的cache添加到result下面
        result = pd.concat([result,cache])

    return result


def main():
    final_result = pd.DataFrame()
    base_url = 'https://book.douban.com/top250?start={}'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    urls = format_url(base_url,pages = 10)
    for url in urls:
        res = parse_page(url,headers = headers)
        final_result = pd.concat([final_result,res])

    #爬虫要文明，这里设置了一个爱心520时间
    time.sleep(5.2)
    return final_result


if __name__ == "__main__":
    final_result = main()