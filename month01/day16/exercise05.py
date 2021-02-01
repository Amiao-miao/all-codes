"""
遍历图形控制器
class GraphicController:
		pass
controller = CommodityController()
controller.add_graphic("圆形")
controller.add_graphic("矩形")
controller.add_graphic ("三角形")

for item in controller:
print(item)
"""
class GraphicIterator:
    def __init__(self,data):
        self.__data=data
        self.__index=-1
        
    def __next__(self):
        self.__index+=1
        if self.__index>len(self.__data)-1:
            raise StopIteration()
        return self.__data[self.__index]


class GraphicController:
    def __init__(self):
        self.__list_graphic=[]

    def add_graphic(self,graphic):
        self.__list_graphic.append(graphic)

    def __iter__(self):
        return GraphicIterator(self.__list_graphic)

controller =GraphicController()
controller.add_graphic("圆形")
controller.add_graphic("矩形")
controller.add_graphic("三角形")

for item in controller:
    print(item)