"""
  主要功能 ：
     接收客户端（浏览器）请求
     解析客户端发送的请求
     根据请求组织数据内容
     将数据内容形成http响应格式返回给浏览器

  特点 ：
     采用IO并发，可以满足多个客户端同时发起请求情况
     通过类接口形式进行功能封装
     做基本的请求解析，根据具体请求返回具体内容，同时可以满足客户端的网页效果加载
"""
from socket import *
from select import select
import re

#具体处理浏览器的http请求，发送响应
class Handle:
    def __init__(self,connfd,html=""):
        self.connfd=connfd
        self.html=html
    #接收并组织请求
    def request(self):
        #data 是http请求
        data = self.connfd.recv(1024*10).decode()
        #获取请求内容
        pattern=r"[A-Z]+\s+(?P<info>/\S*)"
        result=re.match(pattern,data)
        if result:
            info=result.group("info")
            print("请求内容：",info)
            self.send_html(info)

    #组织发送响应
    def send_html(self, info):
        if info=='/':
            filename=self.html+"/index.html"
        else:
            filename=self.html+info
        try:
            file=open(filename,'rb')
        except:
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += "Sorry..."
            response=response.encode()
        else:
            response = "HTTP/1.1 20O OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response = response.encode() + file.read()
        finally:
            self.connfd.send(response)


class WebServer:
    def __init__(self,host="0.0.0.0",port=0,html=""):
        self.host=host
        self.port=port
        self.html=html
        self.rlist=[]
        self.wlist=[]
        self.xlist=[]

        self.sock=self.create_socket()

    # 创建套接字
    def create_socket(self):
        sock=socket()
        self.address=(self.host,self.port)
        sock.bind(self.address)
        sock.setblocking(False)
        return sock

    #处理浏览器连接
    def connect(self):
        connfd,addr=self.sock.accept()
        connfd.setblocking(False)
        self.rlist.append(connfd) #添加浏览器

    def start(self):
        self.sock.listen(5)
        print(f"listen the port {self.port}")
        self.rlist.append(self.sock)
        while True:
            rs,ws,xs=select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                if r is self.sock:
                    self.connect()
                else:
                    self.handle=Handle(r,self.html)
                    self.handle.request()
                    self.rlist.remove(r)
                    r.close()

if __name__ == '__main__':
    #用户如何去做
    #用户决定什么
    httpd=WebServer(host="0.0.0.0",port=8889,html="./static")
    httpd.start() #入口 启动服务