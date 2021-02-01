"""
    商品信息管理系统
"""
class CommodityModel:
    """
        商品数据模型
    """
    def __init__(self, name="", price=0, cid=0):
        self.cid=cid
        self.name=name
        self.price=price

    def __str__(self):
        return f"商品编号为{self.cid},商品名称为{self.name},价格是{self.price}"
    def __eq__(self, other):
        return self.cid==other.cid

class CommodityView:
    """
    商品视图类
    """
    def __init__(self):
        self.__controller=CommodityController()

    def __display_menu(self):
        print("按1键录入商品信息")
        print("按2键显示商品信息")
        print("按3键删除商品信息")
        print("按4键修改商品信息")

    def __select_menu(self):
        item=input("请输入选项：")
        if item=="1":
            self.__input_commodity_info()
        elif item=="2":
            self.__show_commoditiy()
        elif item=="3":
            self.__deleted_commodity()
        elif item=="4":
            self.__modify_student()


    def __input_commodity_info(self):
        commod=CommodityModel()
        commod.name=input("请输入商品名称：")
        commod.price=int(input("请输入商品价格："))
        self.__controller.add_commodity_info(commod)
        print("添加商品信息成功喽！")

    def main(self):
        """
            入口函数
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __show_commoditiy(self):
        for item in self.__controller.list_commodity:
            print(item)

    def __deleted_commodity(self):
        cid=int(input("请输入需要删除的学生的编号:"))
        if self.__controller.remove_commodity(cid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        commodity=CommodityModel()
        commodity.cid=int(input("请输入需要修改的商品编号："))
        commodity.name=input("请输入修改后的商品名称：")
        commodity.price=int(input("请输入修改后的商品价格："))
        if self.__controller.update_commodity(commodity):
            print("更改成功")
        else:
            print("更改失败")


class CommodityController():
    """
        商品信息的控制
    """
    def __init__(self):
        self.__list_commodity=[]
        self.__start_id=1001

    @property
    def list_commodity(self):
        return self.__list_commodity

    def add_commodity_info(self,commod_target):
        commod_target.cid=self.__start_id
        self.__start_id+=1
        self.__list_commodity.append(commod_target)

    def remove_commodity(self, cid):
        commodity=CommodityModel(cid=cid)
        if commodity in self.__list_commodity:
            self.__list_commodity.remove(commodity)
            return True
        else:
            return False

    def update_commodity(self, new_commodity):
        for item in self.__list_commodity:
            if item.cid==new_commodity.cid:
                item.__dict__=new_commodity.__dict__
                return True
        return False


#入口
view=CommodityView()
view.main()