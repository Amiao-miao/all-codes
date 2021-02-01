"""
- 创建网络套接字用于接收客户端请求
- 等待客户端连接
- 客户端连接，则创建新的线程具体处理客户端请求
- 主线程继续等待其他客户端连接
- 如果客户端退出，则销毁对应的线程
"""
import sys
from socket import *
from multiprocessing import Process

HOST='0.0.0.0'
POST=8888
ADDR=(HOST,POST)

#子进程处理客户端请求 入口
def handle(connfd):
    #测试与客户端配合
    while True:
        data=connfd.recv(1024)
        if not data:
            break
        print(data.decode())
    connfd.close()


def main():
    #创建套接字
    sock=socket()
    sock.bind(ADDR)
    sock.listen(5)

    #循环连接客户端
    while True:
        try:
            connfd,addr=sock.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            sock.close()
            sys.exit("服务结束")

        #创建子进程
        p=Process(target=handle,args=(connfd,),daemon=True)
        p.start()

if __name__ == '__main__':
    main()