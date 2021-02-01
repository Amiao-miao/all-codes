"""
以面向对象的思想,描述下列情景.
划分原则：
数据不同使用对象区分——小王
行为不同使用类区分——手机/卫星电话
"""
# (1)需求：小明使用手机打电话
#     识别对象：人类       手机
#     分配职责：打电话      通话
#     建立交互：人类  调用  手机
"""
class People:
    def __init__(self, name=""):
        self.name=name

    def use(self,phone):
        print(self.name,"使用")
        phone.call()


class Phone:

    def call(self):
        print("打电话")

xiaoming=People("小明")
phone=Phone()
xiaoming.use(Phone())
"""
# (2)小明一次请多个保洁打扫卫生
#    效果:调用一次小明通知方法,可以有多个保洁在打扫卫生.

class People:
    def __init__(self, name=""):
        self.name=name

    def engage(self,*args):
        print(self.name,"雇佣")
        for cleaner in args:
            cleaner.cleaning()

class Cleaner:
    def cleaning(self):
        print("打扫卫生")

xiaoming=People("小明")
xiaoming.engage(Cleaner(),
                Cleaner(),
                Cleaner()    )

# (3)张无忌教赵敏九阳神功
#    赵敏教张无忌玉女心经
#    张无忌工作挣了5000元
#    赵敏工作挣了10000元
"""
class Person:
    def __init__(self,name=""):
        self.name=name

    def teach(self,other,skill):
         print(self.name,"在教",other.name,skill)

    def work(self,money):
        print(self.name,"上班赚了",money,"元")

zm=Person("赵敏")
zwj=Person("张无忌")
zwj.teach(zm,"九阳神功")
zm.teach(zwj,"玉女心经")
zwj.work(5000)
zm.work(10000)
"""
