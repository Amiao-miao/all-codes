"""
udp 客户端示例
重点代码 ！！！
"""

from socket import *

#记录服务端地址
ADDR=("176.17.12.168",8886)

#与服务端相同套接字
udp_socket=socket(AF_INET,SOCK_DGRAM)

while True:
    msg=input(">>")
    udp_socket.sendto(msg.encode(),ADDR)
    #客户端直接退出
    if not msg:
        break
    #通过##让服务端退出
    # if msg=='##':
    #     break
    data,addr=udp_socket.recvfrom(1024)
    print("From server:",data.decode())

udp_socket.close()