"""
简单的TCP服务端示例

*同时只能处理一个客户端，
必须一个客户端退出才能处理下一个客户端

*如果tcp循环连续发送时他别容易产生粘包
"""
from socket import *

#创建套接字
from time import sleep

tcp_socket=socket(AF_INET,SOCK_STREAM)

#绑定连接
tcp_socket.bind(("0.0.0.0",8889))

#设置监听
tcp_socket.listen(5)
#连接客户端
while True:
    print("等待客户端连接...")
    connfd,addr=tcp_socket.accept()
    print("连接：",addr)

#先收后发
    while True:
        data=connfd.recv(5)
       #根据特性可知客户端已经退出
        if not data:
            break
        #收到特定字符表示客户端退出
        # if data == b"##":
        #     break
        print("接收到：",data.decode())
        connfd.send(b"ok#")
        sleep(0.1)
    connfd.close()

#关闭套接字

tcp_socket.close()
