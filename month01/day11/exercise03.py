"""
练习1：以面向对象思想,描述下列情景.
小明请保洁打扫卫生
"""
#小明每次雇佣新保洁
"""
class Client:
    def __init__(self, name=""):
        self.name=name

    def engage(self):
        print("雇佣")
        cleaner=Cleaner()
        cleaner.clean()

class Cleaner:
    def clean(self):
        print("打扫")

xiaoming=Client("小明")
xiaoming.engage()
"""

#小明每次雇佣自己的保洁
"""
class Client:
    def __init__(self, name=""):
        self.name=name
        self.__cleaner=Cleaner()
        
    def engage(self):
        print("雇佣")
        self.__cleaner.clean()

class Cleaner:
    def clean(self):
        print("打扫")

xiaoming=Client("小明")
xiaoming.engage()
"""
#小明每次通知传入的参数
class Client:
    def __init__(self, name=""):
        self.name = name

    def engage(self,people):
        print("雇佣")
        people.clean()

class Cleaner:
    def clean(self):
        print("打扫")


xiaoming = Client("小明")
people=Cleaner()
xiaoming.engage(people)


