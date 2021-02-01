"""
练习2:创建技能类，并保护数据在有效范围内
数据：技能名称,冷却时间,  攻击力度,  消耗法力
            0 -- 120  0 -- 200  100 -- 100
"""

class Skill:
    def __init__(self, name="", time=0, atk=0, ap=0):
        self.name=name
        self.cd=time
        self.atk=atk
        self.ap=ap

    @property
    def cd(self):
        return self.__cd

    @cd.setter
    def cd(self, value):
        if 0<=value<=120:
            self.__cd=value
        else:
            raise Exception("冷却时间不足")


    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0<=value<=200:
            self.__atk=value
        else:
            raise Exception("攻击力错误")

    @property
    def ap(self):
        return self.__ap

    @ap.setter
    def ap(self, value):
        if value<0:value=0
        elif value>100:value=100
        self.__ap=value

skill01=Skill("小黑",100,200,500)
print(skill01.name)
print(skill01.cd)
print(skill01.atk)
print(skill01.ap)
