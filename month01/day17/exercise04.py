"""
练习2：在列表中获取所有整数,并计算它的平方.
"""
list01 = [43, "a", 5, True, 6, 7, 89, 9, "b"]

datas=(item**2 for item in list01 if type(item)==int)
tuple_datas=tuple(datas)
print(tuple_datas)