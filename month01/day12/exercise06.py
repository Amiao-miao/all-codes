"""
    练习1：以面向对象思想，描述下列情景：
    情景：手雷爆炸，可能伤害敌人(头顶爆字)或者玩家(碎屏)。
    变化：还可能伤害房子、树、鸭子....
    要求：增加新事物，不影响手雷.
    画出架构设计图
"""
class Mine:
    def __init__(self, atk):
        self.atk=atk
    def explode(self,object):
        print("爆炸")
        object.hurt(self.atk)

class PunchingBag:
    def hurt(self):
        pass

class Enemy(PunchingBag):
    def hurt(self):
        print("头顶爆字")

class Enjoy(PunchingBag):
    def hurt(self):
        print("碎屏")

class House(PunchingBag):
    def hurt(self):
        print("房子")

class Tree(PunchingBag):
    def hurt(self):
        print("树")

class Duck(PunchingBag):
    def hurt(self):
        print("鸭子")

sl=Mine()
house=House()
sl.explode(house)