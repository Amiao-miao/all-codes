"""
    小明使用手机打电话
   要求:增加座机,卫星电话时不影响小明.
"""

class Person:
    def __init__(self, name=""):
        self.name=name
    def use(self, communcation):
        print(self.name,"使用")
        communcation.call()

class Phone:
    def call(self):
        pass

class Seat(Phone):
    def call(self):
        print("座机")

xm=Person("小明")
seat=Seat()
xm.use(seat)


