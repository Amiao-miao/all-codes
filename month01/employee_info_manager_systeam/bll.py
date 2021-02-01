from model import EmployeeModel


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