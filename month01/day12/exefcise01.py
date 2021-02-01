"""
    创建父类：车(品牌，速度)
    创建子类：电动车(电池容量,充电功率)
    创建子类对象并画出内存图。
"""
class Car:
    def __init__(self, brand="", speed=0.0):
        self.brand=brand
        self.speed=speed


class ElectromotionCar(Car):
    def __init__(self, brand="", speed=0.0, battery=0.0, charge=0.0):
        super().__init__(brand, speed)
        self.battery=battery
        self.charge=charge

yadi=ElectromotionCar("雅迪",50,12,46)
print(yadi.brand)
