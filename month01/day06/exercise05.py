"""
        在终端中打印香港字典的所有键(一行一个)
        在终端中打印上海字典的所有值(一行一个)
        在终端中打印新疆字典的所有键和值(一行一个)
        在上海字典中查找值是61对应的键名称
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

for key in dict_xianggang:
    print(key)

for value in dict_shanghai.values():
    print(value)

for k,v in dict_xianggang.items():
    print(k)
    print(v)

for kk,vv in dict_shanghai.items():
    if vv==61:
        print(kk)
        break