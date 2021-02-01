"""
遍历商品控制器
class CommodityController:
		pass
controller = CommodityController()
controller.add_commodity("屠龙刀")
controller.add_commodity("倚天剑")
controller.add_commodity("芭比娃娃")

for item in controller:
    print(item)
"""


class CommodityIterator:
    def __init__(self,data):
        self.__data=data
        self.__index=-1
    def __next__(self):
        self.__index+=1
        if self.__index > len(self.__data) - 1:
            raise StopIteration()
        return self.__data[self.__index]


class CommodityController:
    def __init__(self):
        self.__list_commodity=[]

    def add_commodity(self,commodity):
        self.__list_commodity.append(commodity)

    def __iter__(self):
        return CommodityIterator(self.__list_commodity)

controller = CommodityController()
controller.add_commodity("屠龙刀")
controller.add_commodity("倚天剑")
controller.add_commodity("芭比娃娃")

for item in controller:
    print(item)