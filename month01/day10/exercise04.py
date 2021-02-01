"""
练习1：创建敌人类，并保护数据在有效范围内
          数据:姓名/ 攻击力/  血量
                     0-100   0-500
"""

class Enemy:
    def __init__(self, name="", attack=0, blood=0):
        self.name=name
        self.attack=attack
        self.blood=blood

    @property
    def attack(self):
        return self.__attack
    @attack.setter
    def attack(self,value):
        if 0<=value<=100:
            self.__attack=value
        else:
            raise Exception("错误")

    @property
    def blood(self):
        return self.__blood
    @blood.setter
    def blood(self, value):
        if 0<=value <=500:
            self.__blood = value
        else:
            raise Exception("错误1")

xiaobai=Enemy("小白",2,400)
print(xiaobai.attack)
print(xiaobai.blood)

