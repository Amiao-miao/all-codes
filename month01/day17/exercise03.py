"""
    使用生成器表达式在列表中获取所有字符串.
    list01 = [43, "a", 5, True, 6, 7, 89, 9, "b"]
"""
list01 = [43, "a", 5, True, 6, 7, 89, 9, "b"]
datas=(item for item in list01 if type(item)==str)
tuple_datas=tuple(datas)
print(tuple_datas)