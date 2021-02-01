class EmployeeModel:
    def __init__(self, eid=0, name="", money=0, age=0):
        self.eid=eid
        self.name=name
        self.money=money
        self.age=age
    def __str__(self):
        return f"员工姓名是{self.name},今年{self.age}岁,工资是{self.money}"
    def __eq__(self, other):
        return self.eid==other.eid