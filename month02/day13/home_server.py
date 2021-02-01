from socket import *
from multiprocessing import Process
HOST="0.0.0.0"
PORT=8888
ADDR=(HOST,PORT)



def main():
    sort=socket(AF_INET,SOCK_DGRAM)
    sort.bind(ADDR)

if __name__ == '__main__':
    main()