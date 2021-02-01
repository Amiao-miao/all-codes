dict_employees = {
    1001: {"did": 9002, "name": "师父", "money": 60000},
    1002: {"did": 9001, "name": "孙悟空", "money": 50000},
    1003: {"did": 9002, "name": "猪八戒", "money": 20000},
    1004: {"did": 9001, "name": "沙僧", "money": 30000},
    1005: {"did": 9001, "name": "小白龙", "money": 15000},
}
list_departments = [
    {"did": 9001, "title": "教学部"},
    {"did": 9002, "title": "销售部"},
    {"did": 9003, "title": "品保部"},
]
# 1. 打印所有员工信息,
# 格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
for k,v in dict_employees.items():
    print("%s的员工编号是%d,部门编号是%d,月薪%d元."%
          (v["name"],k,v["did"],v["money"]))
# 2. 打印所有月薪大于2w的员工信息,
# 格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
for key,value in dict_employees.items():
    if value["money"]>20000:
        print("%s的员工编号是%d,部门编号是%d,月薪%d元."%
              (value["name"],key,value["did"],value["money"]))
# 3. 在部门列表中查找编号最小的部门
min_value=list_departments[0]
for i in range(1,len(list_departments)):
    if min_value["did"]>list_departments[i]["did"]:
        min_value=list_departments[i]
print(min_value["title"])
# 4. 根据部门编号对部门列表降序排列
for x in range(len(list_departments)-1):
    for y in range(x+1,len(list_departments)):
        if list_departments[x]["did"]<list_departments[y]["did"]:
            list_departments[x],list_departments[y]=list_departments[y],list_departments[x]
print(list_departments)
