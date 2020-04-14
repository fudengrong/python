
import socket

#创建socket 对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

hostname = socket.gethostname()
#print(hostname)
port = 3306

s.connect((hostname,port))
print(s.recv(1024))

s.close()
#port = socket.getservbyport()
#创建连接
#s.connect(("127.0.0.1",8888))

'''
#接收数据
buffer = []
d = s.recv(1024)
buffer.append(d)

# 把字节连接起来
data = b''.join(buffer)

print(data)

#关闭连接
s.close()

#监听
#s.listen(1)


#while True:
#    sock,addr = s.accept()
#    print('有人进来啦')
#    sock.send(b'hei man ,are you ok')
#    sock.close()

'''

