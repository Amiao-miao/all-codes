
from socket import *

#处理浏览器请求
def http_handle(c):
    data = c.recv(1024 * 10)
    print(data.decode())

    # with open("16.txt") as f:
    with open("timg.jpeg",'rb') as f:
        response = "HTTP/1.1 20O OK\r\n"
        response += "Content-Type:image/jpeg\r\n"
        response += "\r\n"
        response =response.encode()+f.read()
    c.send(response)


def main():
    s=socket()
    s.bind(('0.0.0.0',8884))
    s.listen(5)

    c,addr=s.accept()
    print("Connect from",addr)
    http_handle(c)
    c.close()
    s.close()

if __name__ == '__main__':
    main()


