"""
    面向对象思想,描述下列情景.
    玩家攻击敌人,敌人受伤(根据玩家攻击力，减少敌人的血量).
"""
class Player:
    def __init__(self, attack=0):
        self.attack=attack

    def atk(self,enemy):
        print("攻击")
        enemy.hurt(self.attack)

class Enemy:
    def __init__(self, hp=0):
        self.hp=hp

    def hurt(self,value):
        self.hp -=value
        print("受伤啦，血量还剩",self.hp)

xiaoming=Player(50)
enemy=Enemy(100)
xiaoming.atk(enemy)