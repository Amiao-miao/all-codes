"""
练习2. 基于udp循环收发程序完成

在客户端输入单词，从服务端那里得到单词解释
并打印出来，要求多个客户端可以一起查询

服务端，利用数据库dict->words表 帮助
客户端完成单词查询，将解释发送给客户端
"""
from socket import *
ADDR=("127.0.0.1",8886)

class QueryWord:
    def __init__(self):
        self.udp_socket=socket(AF_INET,SOCK_DGRAM)

    #发送单词得到解释
    def find_word(self, word):
        self.udp_socket.sendto(word.encode(), ADDR)
        data, addr = self.udp_socket.recvfrom(1024)
        return data.decode()

    # 输入和输入控制
    def query_word(self):
        while True:
            #将输入的单词发送给服务端
            word=input("请输入单词：")
            #客户端直接退出
            if not word:
                break
            mean=self.find_word(word)
            print("%s : %s"%(word, mean))

    def close(self):
        self.udp_socket.close()

if __name__ == '__main__':
    query=QueryWord()