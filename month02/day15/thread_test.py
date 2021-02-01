"""
tcp 套接字 客户端示例
"""

from socket import *

#服务器地址
ADDR=("127.0.0.1",8888)

#默认就是tcp
tcp_socket=socket()

#连接服务器
tcp_socket.connect(ADDR)

#先发送再接收
while True:
    msg=input("请输入：")
    if not msg:
        break
    tcp_socket.send(msg.encode())

#关闭
tcp_socket.close()
