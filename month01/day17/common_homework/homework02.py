"""
需求：
        定义函数，在员工列表中查找员工编号最小的员工
        定义函数，在员工列表中查找薪资最少的员工
    步骤：
        1. 根据需求，写出函数。
        2. 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(分、隔、做)
           创建通用函数get_min(定义到单独模块中)
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

# 查找员工编号最小的员工
# def find01():
#     min_eid=list_employees[0]
#     for item in range(1,len(list_employees)):
#         if min_eid.eid>list_employees[item].eid:
#             min_eid=list_employees[item]
#     return min_eid
# # 在员工列表中查找薪资最少的员工
# def find02():
#     min_money=list_employees[0]
#     for item in range(1,len(list_employees)):
#         if min_money.money>list_employees[item].money:
#             min_money=list_employees[item]
#     return min_money

# def condition01(min_eid):
#     return min_eid.eid
#
# def condition02(min_money):
#     return min_money.money

# def get_min(func):
#     min_value = list_employees[0]
#     for item in range(1,len(list_employees)):
#         if func(min_value)>list_employees[item].money:
#             min_value=list_employees[item]
#     return min_value

min01=IterableHelper.get_min(list_employees,lambda min_eid:min_eid.eid)
print(min01.__dict__)

min02=IterableHelper.get_min(list_employees,lambda min_money:min_money.money)
print(min02.__dict__)
