"""
练习：创建手机类
      数据：品牌、价格、颜色
      行为：通话
      实例化两个对象并调用其函数
      画出内存图
"""

class Phone:

    def __init__(self,quality,price,color):
        self.quality=quality
        self.price=price
        self.color=color

    def call(self):
        print(self.quality+"通话")

iphone=Phone("苹果",10000,"绿色")
print(iphone.price)