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
#         if item.eid==1003:
#             return item
#
# def find02():
#     for item in list_employees:
#         if item.name=="孙悟空":
#             return item


# def condtion01(item):
#     return item.eid==1003


# def condtion02(item):
#     return item.name=="孙悟空"

# def find_single(func):
#     for item in list_employees:
#         if func(item):
#             return item
#
# emp=find_single(lambda item:item.eid==1003)
# print(emp.__dict__)
#
# emp=find_single(lambda item:item.name=="孙悟空")
# print(emp.__dict__)