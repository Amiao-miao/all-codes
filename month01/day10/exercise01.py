"""
创建狗类
数据：品种、昵称、身长、体重
    行为：吃(体重增长1)
    实例化两个对象并调用其函数
    画出内存图
"""

class Dog:
    def __init__(self, breed="", nickname="", height=0, weight=0):
        self.breed=breed
        self.nickname=nickname
        self.height=height
        self.weight=weight

    def eat(self):
        print("吃")
        self.weight+=1

jinmao=Dog("金毛","小董",50,60)
jinmao.eat()
print(jinmao.weight)

keji=Dog("柯基","小白",30,40)
keji.eat()
print(keji.weight)