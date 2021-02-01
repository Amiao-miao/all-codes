"""
    练习：
        创建子类：狗(跑)，鸟类(飞)
        创建父类：动物(吃)
        体会子类复用父类方法
        体会 isinstance 、issubclass 与 type 的作用.
"""

class Animal:
    def ert(self):
        print("吃")

class Dog(Animal):
    def run(self):
        print("跑")

class Bird(Animal):
    def fly(self):
        print("飞")

dog=Dog()
bird=Bird()
bird.ert()

print(isinstance(dog,Animal))
print(isinstance(bird,Dog))
print(issubclass(Dog,Animal))
print(issubclass(Animal,Dog))
print(type(dog)==Dog)
print(type(dog)==Bird)