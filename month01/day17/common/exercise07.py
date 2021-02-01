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
# def find01():
#     for item in list_employees:
#         yield item.name
#
#
# def find02():
#     for item in list_employees:
#         yield item.eid,item.money

# def condtion01(number):
#     return number.name
#
#
# def condtion02(number):
#     return number.eid,number.money



for name in IterableHelper.select(list_employees,lambda number:number.name):
    print(name)

for item in IterableHelper.select(list_employees,lambda number:(number.eid,number.money)):
    print(item)