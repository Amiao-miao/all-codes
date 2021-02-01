"""
        在终端中打印香港的现有人数
        在终端中打印上海的新增和现有人数
        新疆新增人数增加1
"""

dict_xianggang={
        "region":"香港",
        "new":15,
        "now":393,
        "total":4801,
        "cure":4320,
        "death":88}

dict_shanghai={"region":"上海","new":6,"now":61,"total":903,"cure":835,"death":7}
dict_xinjiang={"region":"新疆","new":0,"now":49,"total":902,"cure":850,"death":3}

print(f"香港的现有人数:dict_xianggang['now']")
print(dict_shanghai["new"])
print(dict_shanghai["now"])
dict_xinjiang["new"]+=1