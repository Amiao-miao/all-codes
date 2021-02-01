from  socket import *
from time import localtime

#接收文件
def recv_image(connfd):
    #组织文件名
    filename= "%s-%s-%s"%localtime()[:3]+".jpg"
    file = open(filename, "wb")
    while True:
        #边收边写
        data = connfd.recv(1024)
        if not data:
            break
        file.write(data)
    file.close()
    connfd.close()


def main():
    tcp_socket=socket()
    tcp_socket.bind(("0.0.0.0",8888))
    tcp_socket.listen(5)

    while True:
        connfd,addr=tcp_socket.accept()
        print("地址是：",addr)
        recv_image(connfd)

if __name__ == '__main__':
    main()