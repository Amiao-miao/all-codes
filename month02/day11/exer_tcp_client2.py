from socket import *

ADDR=("127.0.0.1",8888)

def chat(msg):
    tcp_socket = socket()
    tcp_socket.connect(ADDR)
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    tcp_socket.close()
    return data.decode()
def main():
    while True:
        msg=input("我:")
        if not msg:
            break
        print("mm:",chat(msg))

if __name__ == '__main__':
    main()
