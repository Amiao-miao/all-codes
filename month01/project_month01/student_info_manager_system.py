"""

    餐厅架构
        迎宾 -- 点餐服务员 -- 厨师 -- 送菜服务员
    软件架构
        视图View                控制Controller
            界面逻辑(输入输出)        业务逻辑(核心算法)

                    模型Model
                        数据抽象
"""


# 学生信息管理系统
# 商品
# 疫情
# 员工
# ...
class StudentModel:
    """
        学生数据模型
    """

    def __init__(self, name="", age=0, score=0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        # 编号(对学生信息的唯一标记)
        self.sid = sid


class StudentView:
    """
        学生视图类
    """

    def __init__(self):
        self.__controller = StudentController()

    def __display_menu(self):
        print("按1键录入学生信息")
        print("按2键显示学生信息")
        print("按3键删除学生信息")
        print("按4键修改学生信息")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            # 自动生成参数/函数:alt + 回车
            self.__input_student_info()

    def __input_student_info(self):
        stu = StudentModel()
        stu.name = input("请输入学生姓名:")
        stu.age = int(input("请输入学生年龄:"))
        stu.score = int(input("请输入学生成绩:"))
        self.__controller.add_student_info(stu)
        print("添加学生成功喽")

    def main(self):
        """
            入口函数
        """
        while True:
            self.__display_menu()
            self.__select_menu()


class StudentController:
    """
        学生信息的控制
    """

    def add_student_info(self, stu_target):
        pass


# 入口
view = StudentView()
view.main()