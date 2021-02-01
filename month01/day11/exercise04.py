"""
练习3：以面向对象思想,描述下列情景.
玩家攻击敌人,敌人受伤(头顶爆字).
"""

class Player:
    def atk(self,enemy):
        print("攻击")
        enemy.hurt()

class Enemy:
    def hurt(self):
        print("受伤")

xiaoming=Player()
enemy=Enemy()

xiaoming.atk(enemy)
