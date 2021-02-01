

class StudentView:

    def __dispaly_menu(self):
        print("按1键录入学生信息")
        print("按2键显示学生信息")
        print("按3键删除学生信息")
        print("按4键修改学生信息")

    def __select_menu(self):
        item=input("请输入选项：")
        if item=="1":
            self.__input_student()

    def __input_student(self):
        pass