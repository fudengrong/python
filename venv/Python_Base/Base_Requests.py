import  requests

#reponse = requests.get('https://www.zhihu.com/',headers=headers)
#requests.get('http://httpbin.org/cookies/set/number/123456789')
#reponse = requests.get('http://httpbin.org/cookies')
#print(reponse.text)

#s = requests.Session()
#s.get('http://httpbin.org/cookies/set/number/123456789')
#reponse = s.get('http://httpbin.org/cookies')
#print(reponse.text)
'''
headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Host": "httpbin.org",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-5e7b1335-3732edad6ba9ef1dee8cada6"
  }
'''
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
#reponse = requests.get('https://www.zhihu.com/explore',headers=headers)
reponse = requests.get('https://www.baidu.com/',headers=headers)

print(reponse.text)
print('#'*30)
print(reponse.status_code)
#print(reponse.cookies)
#print(reponse.headers)

#for key,value in reponse.cookies.items():
#    print(key+'='+value)
