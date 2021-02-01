"""
分为服务端和客户端，要求可以有多个客户端同时操作。
客户端可以查看服务器文件库中有什么文件。
客户端可以从文件库中下载文件到本地。
客户端可以上传一个本地文件到文件库。
使用print在客户端打印命令输入提示，引导操作
"""
import os
from socket import *
from threading import Thread
from time import sleep

# 文件库
FTP = "/home/tarena/FTP/"

# 具体处理客户端事务
class Handle:
    def __init__(self, connfd):
        self.connfd=connfd

    def do_list(self):
        files = os.listdir(FTP)
        if files:
            self.connfd.send(b"OK")
            sleep(0.1)
            # 组合所有文件名
            data = "\n".join(files)
            self.connfd.send(data.encode())
        else:
            self.connfd.send(b"FAIL")

    def do_get(self,filename):
        try:
            file=open(FTP+filename,'rb')
        except Exception:
            self.connfd.send(b'FAIL')
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
            #发送文件
            while True:
                data=file.read(1024)
                if not data:
                    break
                self.connfd.send(data)
            sleep(0.1)
            self.connfd.send(b"##")
            file.close()


    def do_Put(self,filename):
        #打开文件判断是否存在
        try:
            file=open(filename,'rb')
        except Exception:
            print("没有该文件")
            return
        #提取真正的文件名
        filename=filename.split("/")[-1]
        data="PUT "+filename
        self.sock.send(data.encode())
        #等待响应
        result=self.sock

    def request(self,data):

        if data=="LIST":
            self.do_list()
        elif data[:3] == "GET":
            filename=data.split(' ')[-1]
            self.do_get(filename)
        elif data[:3] == "PUT":
            filename=data.split(' ')[-1]
            self.do_Put(filename)
        elif data == "EXIT":
            pass




#为每个客户端创建线程
class ClientThread(Thread):
    def __init__(self,connfd):
        self.connfd=connfd
        self.handle=Handle(connfd)
        super().__init__(daemon=True)

    def run(self):
        while True:
            data=self.connfd.recv(1024).decode()
            if not data:
                break
            self.handle.request(data)
        self.connfd.close()


#并发服务类
class ConcurrentServer:
    """
    提供并发服务
    """
    def __init__(self,host="",port=0):
        self.host=host
        self.port=port
        self.address=(host,port)
        self.__sock=self.__create_socket()

    # 创建套接字
    def __create_socket(self):
        tcp_socket = socket()
        tcp_socket.bind(self.address)
        return tcp_socket
    #启动服务
    def serve_forver(self):
        print(f"listen the port {self.port}")
        self.__sock.listen(5)
        while True:
            connfd,addr=self.__sock.accept()
            print("Connect from ",addr)
            #为客户端创建线程
            t=ClientThread(connfd)
            t.start()

if __name__ == '__main__':
    server=ConcurrentServer(host="0.0.0.0",port=8888)
    server.serve_forver()