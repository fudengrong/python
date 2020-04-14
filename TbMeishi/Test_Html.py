from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
from pyquery import PyQuery as pq


browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)

browser.get('https://s.taobao.com/search?q=%E7%BE%8E%E9%A3%9F&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=-12&ntoffset=-12&p4ppushleft=1%2C48&s=264')
#/html/body/div[1]/div[2]/div[3]/div[1]/div[21]
def get_products():
    #print('正在获取商品明细')
    wait.until(EC.presence_of_element_located((By.CLASS_NAME,'#m-itemlist .items .item')))###mainsrp-itemlist
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist.items.item').items()
    for item in items:
        product = {
            'image':item.find('.pic.img').attr('src'),
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text()[:-3],
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
        }
        print(product)

#content-wrap .house-list-wrap .sendsoj