"""
使用封装数据的思想
   创建员工类/部门类,修改实现下列功能.
    1. 定义函数,打印所有员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
    2. 定义函数,打印所有月薪大于2w的员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
    3. 定义函数,打印所有员工的部门信息,格式：xx的部门是xx,月薪xx元.
    4. 定义函数,查找薪资最少的员工
    5. 定义函数,根据薪资对员工列表升序排列
"""

class Employees:
    def __init__(self, eid=0, did=0, name="", money=0):
        self.eid=eid
        self.did=did
        self.name=name
        self.money=money

class Departments:
    def __init__(self, did=0, title=""):
        self.did=did
        self.title=title

list_employees = [
    Employees(1001,9002,"师父",60000),
    Employees(1002,9001,"孙悟空",50000),
    Employees(1003,9002,"猪八戒",20000),
    Employees(1004,9001,"沙僧",30000),
    Employees(1005,9001,"小白龙",15000),
]
list_departments =[
    Departments(9001,"教学部"),
    Departments(9002,"销售部")
]

def print_sigle_employees(employees):
    print(f"{employees.name}的员工编号是{employees.eid},部门编号是{employees.did},月薪{employees.money}元")
# 1. 定义函数,打印所有员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
def print_all_employees():
    for employees in list_employees:
        print_sigle_employees(employees)
print_all_employees()
# 2. 定义函数,打印所有月薪大于2w的员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
def print_gt_2w_employees():
    for employees in list_employees:
        if employees.money>20000:
            print_sigle_employees(employees)
print_gt_2w_employees()
# 3. 定义函数,打印所有员工的部门信息,格式：xx的部门是xx,月薪xx元.
def print_all_departments():
    for employees in list_employees:
        for departments in list_departments:
            if employees.did==departments.did:
                print(f"{employees.name}的部门是{departments.title},月薪{employees.money}元")
                break
print_all_departments()
# 4. 定义函数,查找薪资最少的员工
def gt_min_money():
    min_money=list_employees[0]
    for item in range(1,len(list_employees)):
        if min_money.money>list_employees[item].money:
            min_money=list_employees[item]
    return min_money
print(gt_min_money().__dict__)
# 5. 定义函数,根据薪资对员工列表升序排列
def asc_by_money():
    for r in range(len(list_employees)-1):
        for c in range(r+1,len(list_employees)):
            if list_employees[r].money>list_employees[c].money:
                list_employees[r],list_employees[c]=list_employees[c],list_employees[r]
asc_by_money()
print(list_employees)
for item in list_employees:
    print(item.__dict__)