import requests
import re
import json

url = 'http://bang.dangdang.com/books/hotbang'
respose = requests.get(url).text
resloue =()

'''
def request_dandan(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parse_result(html):
    print(html).text
    pattern = re.compile(
        '<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">¥(.*?)</span>.*?</li>',
        re.S)
    items = re.findall(pattern, html)
'''