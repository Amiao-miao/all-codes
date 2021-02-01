"""
    需求：
        定义函数，根据薪资对员工列表进行升序排列
        定义函数，根据员工编号对员工列表进行升序排列
    步骤：
        1. 根据需求，写出函数。
        2. 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(分、隔、做)
           创建通用函数order_by(定义到单独模块中)
        3. 在当前模块中调用(使用lambda)
"""
from iterable_tools import IterableHelper


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money
    def __str__(self):
        return f"员工编号是{self.eid},部门编号{self.did},员工姓名为{self.name},薪资是{self.money}"
list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]
# # 薪资对员工列表进行升序排列


# def get_des01():
#     for r in range(len(list_employees)-1):
#         for c in range(r+1,len(list_employees)):
#             if list_employees[r].money >list_employees[c].money:
#                 list_employees[r],list_employees[c]=list_employees[c],list_employees[r]
# get_des01()
# print(list_employees)

# # 员工编号对员工列表进行升序排列
# def get_des02():
#     for r in range(len(list_employees)-1):
#         for c in range(r+1,len(list_employees)):
#             if list_employees[r].eid >list_employees[c].eid:
#                 list_employees[r],list_employees[c]=list_employees[c],list_employees[r]
#     yield list_employees

# def condition01(item):
#     return item.money
#
# def condition02(item):
#     return item.eid

# def order_by(func):
#     for r in range(len(list_employees)-1):
#         for c in range(r+1,len(list_employees)):
#             if func(list_employees[r]) >func(list_employees[c]):
#                 list_employees[r],list_employees[c]=list_employees[c],list_employees[r]

IterableHelper.order_by(list_employees,lambda item:item.money)
print(list_employees)
for item in list_employees:
    print(item)

IterableHelper.order_by(list_employees,lambda item:item.eid)
print(list_employees)
for item in list_employees:
    print(item)