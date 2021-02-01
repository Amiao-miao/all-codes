"""
对象计数器
统计构造函数执行的次数
        使用类变量实现
		画出内存图
class Wife:
    pass

w01 = Wife("双儿")
w02 = Wife("阿珂")
w03 = Wife("苏荃")
w04 = Wife("丽丽")
w05 = Wife("芳芳")
print(w05.count) # 5
Wife.print_count()# 总共娶了5个老婆
"""

class Wife:
    count=0   #类变量：不同对象的相同数据
    @classmethod
    def print_count(cls):
        print(f"总共娶了{cls.count}个老婆")
    def __init__(self,name):
        self.name=name     #实例变量：不同对象的不同数据
        Wife.count+=1
w01=Wife("双儿")
print(w01.count)
Wife.print_count()