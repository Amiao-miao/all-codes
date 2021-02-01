"""
    直接打印商品对象: xx的编号是xx,单价是xx
    直接打印敌人对象: xx的攻击力是xx,血量是xx

class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

class Enemy:
    def __init__(self, name="", atk=0, hp=0):
        self.name = name
        self.atk = atk
        self.hp = hp
"""
class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name}的编号是{self.cid},单价是{self.price}"

c01=Commodity(1001,"小馒头",10)
print(c01)

class Enemy:
    def __init__(self, name="", atk=0, hp=0):
        self.name = name
        self.atk = atk
        self.hp = hp
    def __str__(self):
        return f"{self.name}的攻击力是{self.atk},血量是{self.hp}"

e01=Enemy("降龙十八掌",30,100)
print(e01)