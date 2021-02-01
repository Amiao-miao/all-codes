"""
删除列表重复数列
[4,35,7,64,7,35]
"""
#
# list01=[4,35,7,64,7,35]
# set01=set(list01)
# res=list(set01)
# print(res)

def get_list(list01):
    set01 = set(list01)
    res = list(set01)
    return res

result=get_list([4,35,7,64,7,35])
print(result)