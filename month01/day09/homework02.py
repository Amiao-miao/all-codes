"""
面向对象
   创建桌子类
        数据：品牌,材质,尺寸(长,宽,高)
   创建电脑类
        数据:型号,CPU型号,内存大小,硬盘大小
        行为：开机,关机
"""

class Desk:
    def __init__(self,brand="",material="",size=()):
        self.brand=brand
        self.material=material
        self.size=size

lege=Desk("乐哥","复合材质",(50,20,10))
