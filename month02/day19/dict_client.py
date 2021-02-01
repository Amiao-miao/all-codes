"""
客户端请求操作  --> 2个界面
"""
import sys
from socket import *

ADDR=('127.0.0.1',8000)

class DictRequest:
    def __init__(self):
        self.sock=self.create_socket()

    def create_socket(self):
        sock=socket()
        sock.connect(ADDR)
        return sock

    def do_register(self):
        while True:
            name=input("Name:")
            passwd=input("Password:")

            if " " in name or " " in passwd:
                print("用户名或密码不能有空格")
                continue

            #发送请求
            msg=f"R {name} {passwd}"
            self.sock.send(msg.encode())
            #等待响应
            result=self.sock.recv(128)
            if result==b"OK":
                print("注册成功")
                return name
            else:
                print("注册失败")
            return

    def do_login(self):
        name=input("请输入用户名：")
        passwd=input("请输入密码：")
        msg=f"L {name} {passwd}"
        self.sock.send(msg.encode())
        # 等待响应
        result = self.sock.recv(128)
        if result == b"OK":
            print("登录成功")
            return name
        else:
            print("登录失败")


    def do_exit(self):
        self.sock.send(b"E")

    def do_query(self, name):
        while True:
            word=input("请输入想要查询的单词：")
            if word=="##":
                break
            msg=f"Q {name} {word}"
            self.sock.send(msg.encode())
            #无论是否查到都打印返回结果
            result=self.sock.recv(1024*10)
            print(result.decode())

    def do_hist(self, name):
        msg="H "+name
        self.sock.send(msg.encode())
        while True:
            data=self.sock.recv(1024).decode()



class DictView:
    def __init__(self):
        self.request=DictRequest()

    def login_menu(self,name):
        while True:
            print("\n*** 查  询 ***")
            print("  1) 查询单词")
            print("  2) 历史记录")
            print("  3) 注   销")
            print("*******User:%s******\n"%name)
            item = input("请输入选项：")
            if item == '1':
                self.request.do_query(name)
            elif item == '2':
                self.request.do_hist(name)
            elif item == '3':
                break
            else:
                print("请重新输入选项！")

    def __diplay_menu(self):
        print("\n*** 首  页 ***")
        print("  1) 登  录")
        print("  2) 注  册")
        print("  3) 退  出")
        print("")

    def __select_menu(self):
        item = input("请输入选项：")
        if item == '1':
            name=self.request.do_login()
            if name:
                self.login_menu(name)
        elif item == '2':
            self.request.do_register()
        elif item == '3':
            self.request.do_exit()
            sys.exit("谢谢使用")
        else:
            print("请重新输入选项！")

    def main(self):
        while True:
            self.__diplay_menu()
            self.__select_menu()


if __name__ == '__main__':
    view=DictView()
    view.main()