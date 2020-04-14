'''
try:
   with open('F:\111.txt','r',encoding='utf-8') as f:
       f.read()
except IOError:
    print ("Error: 没有找到文件或读取文件失败")
else:
    f.close()
'''
try:
    name = ['A','b','c']
    name[4]
except IndexError:
    print('value err ')