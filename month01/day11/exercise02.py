"""
只读属性
创建桌子类
    数据：品牌，材质，尺寸（长，宽，高）
"""

class Desk:
    def __init__(self):
        self.__quality="乐哥"
        self.__material="复合材质"
        self.__size=(50,20,10)

    @property
    def quality(self):
        return self.__quality

    @property
    def material(self):
        return self.__material

    @property
    def size(self):
        return self.__size

