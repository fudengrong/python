# _*_ coding:utf-8 _*_
'''
#测试向文件中读写内容
try:
    f = open('E:/1.txt','w',encoding='utf-8')
    #f = open('E:/1.txt','r',encoding='utf-8')
    print(f.write('测试向文件中写入内容：结束啦  哈哈哈'))
    #print(f.read())

finally:
    if f:
        f.close()

# 对文件进行读写的简易写法
with open('E:/1.txt','a',encoding='utf-8') as f:
    print(f.write('\n换行输入字符串测试1'))

'''

#导入文件存储模块
import pickle as p

# 我们要存储内容的文件名
girlfriendlistfile = 'girlfrien.data'

girlfriends = ['A','B','C']

with open(girlfriendlistfile,'wb+') as f:
    p.dump(girlfriends,f)


#删除文件中内容
del girlfriends

with open(girlfriendlistfile,'rd+') as f:
    list = p.load(f)
    print(list)


