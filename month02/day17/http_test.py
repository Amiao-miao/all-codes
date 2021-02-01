"""
获取Http请求和响应
"""

from socket import *

s=socket()
s.bind(('0.0.0.0',8888))
s.listen(5)

c,addr=s.accept()
print("Connect from",addr)

data=c.recv(1024*10)
print(data.decode())

response="HTTP/1.1 20O OK\r\n"
response+="Content-Type:text/html;charset=utf-8\r\n"
response+="\r\n"
response+="好"


c.send(response.encode())

c.close()
s.close()