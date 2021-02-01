"""
    创建图形管理器
	1. 记录多种图形（圆形、矩形....）
	2. 提供计算总面积的方法.
    满足：
        开闭原则
    测试：
        创建图形管理器，存储多个图形对象。
        通过图形管理器，调用计算总面积方法.
"""

class FigureManager:
    def __init__(self):
        self.__all_figure=[]

    def add_figure(self,figure):
        if isinstance(figure,Figure):
            self.__all_figure.append(figure)

    def get_total_acreage(self):
        total_acreage=0
        for item in self.__all_figure:
            total_acreage+=item.calculate_acreage()
        return total_acreage


class Figure:
    def calculate_acreage(self):
        pass


class Rotundity(Figure):
    def __init__(self,r):
        self.r=r

    def calculate_acreage(self):
        return 3.14*self.r**2

class Rectangle(Figure):
    def __init__(self, height, width):
        self.heihet=height
        self.width=width

    def calculate_acreage(self):
        return self.heihet*self.width

manager=FigureManager()
manager.add_figure(Rotundity(10))
manager.add_figure(Rectangle(4,5))
manager.add_figure("三角")
print(manager.get_total_acreage())
