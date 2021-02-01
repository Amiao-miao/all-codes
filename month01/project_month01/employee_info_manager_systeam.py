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

class EmployeeView:
    def __init__(self):
        self.__controller=EmployeeController()

    def __display_menu(self):
        print("按1录入员工信息")
        print("按2显示员工信息")
        print("按3删除员工信息")
        print("按4修改员工信息")

    def __select_menu(self):
        item=input("请输入选项：")
        if item=="1":
            self.__input_employee_info()
        if item=="2":
            self.__show_employee()
        if item=="3":
            self.__deleted_employee()
        if item=="4":
            self.__modify_employee()

    def __input_employee_info(self):
        employee=EmployeeModel()
        employee.name=input("请输入姓名：")
        employee.money=input("请输入工资：")
        employee.age=input("请输入年龄：")
        self.__controller.add_employee_info(employee)
        print("录入成功啦！")

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __show_employee(self):
        for item in self.__controller.list_employee:
            print(item)

    def __deleted_employee(self):
        eid=int(input("请输入需要删除的员工信息："))
        if self.__controller.remove_employee(eid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_employee(self):
        employee=EmployeeModel()
        employee.eid=int(input("请重新输入员工编号："))
        employee.name=input("请重新输入员工姓名：")
        employee.age=int(input("请重新输入员工年龄："))
        employee.money=int(input("请重新输入员工工资："))
        if self.__controller.updte_employee(employee):
            print("修改成功")
        else:
            print("修改失败")

class EmployeeController:
    def __init__(self):
        self.__list_employee=[]
        self.__start_id=1001

    @property
    def list_employee(self):
        return self.__list_employee

    def add_employee_info(self,employee_target):
        employee_target.eid=self.__start_id
        self.__start_id+=1
        self.__list_employee.append(employee_target)

    def remove_employee(self, eid):
        employee=EmployeeModel(eid)
        if employee in self.__list_employee:
            self.__list_employee.remove(employee)
            return True
        else:
            return False

    def updte_employee(self,new_employee):
        for item in self.__list_employee:
            if item.eid==new_employee.eid:
                item.__dict__=new_employee.__dict__
                return True
        return False



view=EmployeeView()
view.main()
