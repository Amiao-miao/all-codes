"""
多进程 tcp 并发服务
"""

from socket import *
from multiprocessing import Process
from dict_database import Database

class DictHandle:
    def __init__(self,connfd):
        self.connfd=connfd

    def do_register(self,name,passwd):
        if db.register(name,passwd):
            self.connfd.send(b"OK")
        else:
            self.connfd.send(b"FAIL")

    def do_login(self, name, passwd):
        if db.login(name, passwd):
            self.connfd.send(b"OK")
        else:
            self.connfd.send(b"FAIL")

    def do_query(self,word):
        mean=db.query(word)
        data=f"{word} : {mean}"
        self.connfd.send(data.encode())

    def request(self,data):
        tmp = data.split(' ')
        if tmp[0] == "R":
            self.do_register(tmp[1],tmp[2])
        elif tmp[0]=='L':
            self.do_login(tmp[1], tmp[2])
        elif tmp[0]=='Q':
            self.do_query(tmp[1])




# 进程类负责创建进程
class DictProcess(Process):
    def __init__(self,connfd):
        self.connfd=connfd
        self.handle=DictHandle(connfd)
        super().__init__(daemon=True)

    def run(self):
        db.course()#每个进程创建一个游标
        #循环接收请求
        while True:
            request=self.connfd.recv(1024).decode()
            if not request or request=='E':
                break
            else:
                self.handle.request(request)


        db.cur.close()
        self.connfd.close()



#server类负责网络搭建
class DictServer:
    def __init__(self, host="", port=8000):
        self.host=host
        self.port=port
        self.db=Database()
        self.sock=self.create_socket()

    #创建tcp套接字
    def create_socket(self):
        sock=socket()
        self.address=(self.host,self.port)
        sock.bind(self.address)
        return sock

    def serve_forever(self):
        self.sock.listen(5)
        print(f"Listen the port {self.port}")
        #循环处理连接
        while True:
            try:
                connfd,addr=self.sock.accept()
                print(f"Connect from ",addr)
            except KeyboardInterrupt:
                db.close()
                self.sock.close()
                return
            p=DictProcess(connfd)
            p.start()


if __name__ == '__main__':
    dict=DictServer(host='0.0.0.0',port=8000)
    db=Database()
    dict.serve_forever()
