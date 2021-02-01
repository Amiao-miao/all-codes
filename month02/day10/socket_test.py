"""
套接字 基础函数示例
"""

import socket

#创建udp套接字
udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#绑定地址
#①本地地址  127.0.0.1或localhost
#要求另外一端必须也在该计算机上才能访问
# udp_socket.bind(("127.0.0.1",8888))

# ②.网络地址
#要求另外一端通过网络IP访问，可以在其他计算机上
# udp_socket.bind(("176.17.12.208",8888))

# ③.0.0.0.0
#等同于127.0.0.1+176.17.12.208
udp_socket.bind(("0.0.0.0",8886))