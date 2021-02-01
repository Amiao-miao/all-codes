"""
udp套接字服务端模型
重点代码
"""

from socket import *

udp_socket=socket(AF_INET,SOCK_DGRAM)
udp_socket.bind(("0.0.0.0",8886))
while True:
    data,addr=udp_socket.recvfrom(1024)
    # if data==b'##':
    #     break
    print("From",addr,":",data.decode())

    n=udp_socket.sendto("你是个kitty吧吧".encode(),addr)
    print("发送了%d个字节"%n)

udp_socket.close()
