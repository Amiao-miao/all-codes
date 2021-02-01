"""
 需求：
        定义函数，在员工列表中查找所有薪资大于20000的员工数量
        定义函数，在员工列表中查找所有部门编号是9001的员工数量
    步骤：
        1. 根据需求，写出函数。
        2. 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(分、隔、做)
           创建通用函数get_count(定义到单独模块中)
        3. 在当前模块中调用(使用lambda)
"""
from iterable_tools import IterableHelper


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money

list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]
# 找所有薪资大于20000的员工数量
# def find01():
#     count=0
#     for item in list_employees:
#         if item.money>20000:
#             count+=1
#     return count
#
# # 查找所有部门编号是9001的员工数量
# def find02():
#     count=0
#     for item in list_employees:
#         if item.did==9001:
#             count+=1
#     return count

# def condition01(item):
#     return item.money>20000
#
# def condition02(item):
#     return item.did==9001
#
# def get_count(func):
#     count = 0
#     for item in list_employees:
#         if func(item):
#             count += 1
#     return count

count1=IterableHelper.get_count(list_employees,lambda item:item.money>20000)
print(count1)

count2=IterableHelper.get_count(list_employees,lambda item:item.did==9001)
print(count2)