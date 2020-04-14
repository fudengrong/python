# _*_ conding:utf-8 _*_
'''
程序目的：实战爬去淘宝美食数据 保存到mongodb上
所需架包：selenium，pyquery，chromedriver,phantomjs,pymongo
实现逻辑：
1、selenium利用浏览器驱动程序进行搜索
2、分析页码并翻页，
3、分析和提取商品内容，利用pyquery分析源码解析到到商品列表
4、将商品信息存储到数据库中
注意：在整个编译过程中切忌要注意空格
'''
#引入架包
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
from pyquery import PyQuery as pq
import pymongo

#通过phantomjs 控制加载图片和缓存,由于淘宝登录需要手机验证才能进行收索，所有隐藏chrome浏览器未实现
SERVICE_ARGS = ['--load-images=false','--disk-cache=true']
#browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
browser.set_window_size(1400,900)


#MONGODB基础信息
MONMGO_URL = '127.0.0.1'
MONMGO_DB = 'taobao'
MONMGO_TABLE = 'product'

client = pymongo.MongoClient(MONMGO_URL)
db = client[MONMGO_DB]

#定义收索方法
def search():
    print('正在收索')
    try:
        # 收索框
        browser.get('https://www.taobao.com/')
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))
        )
        # 淘宝首页收索后-收索按钮 #J_SearchForm > button  #J_SearchForm > button
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        #输入收索关键字
        input.send_keys('美食')
        #点击收索
        submit.click()
        #获取收索结果总页数
        total = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
        return total.text
        get_products()
    except TimeoutException:
        return search()
#定义页码方法
def next_page(page_number):
    print('当前翻页',page_number)
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input"))
        )
        # 淘宝首页收索后-提交按钮
        submit = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page_number)))
            #(By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.next > a > span:nth-child(1)'), str(page_number)))
        get_products()
    except TimeoutException:
        next_page(page_number)
#获取商品信息方法
def get_products():
    #print('正在获取商品明细')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item')))
    # print(reslut)
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
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
        save_to_mongodb(product)
#定义数据保存方法
def save_to_mongodb(result):
    try:
        if db[MONMGO_TABLE].insert(result):
            print('保存MONGODB成功', result)
    except Exception:
        print('保存MONGODB失败',result)

def main():
    try:
        total = search()
        total = int(re.compile('(\d+)').search(total).group(1))
        for i in range(2, total + 1):
            next_page(i)
    finally:
        browser.close()



if __name__=='__main__':
    main()

