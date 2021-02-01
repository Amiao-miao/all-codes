"""
    定义函数,将列表中奇数删除
    测试数据:[3,7,5,6,7,8,9,13] --> [6,8]
    提示:在列表中删除多个元素,倒序删除
"""
# 列表删除一个数据，后面的数据就会往前挤
# list01=[3,7,5,6,7,8,9,13]
# for i in range(len(list01)):
#     if list01[i]%2:
#         del list01[i]
# print(list01)



# 根据条件在容器中删除多个元素
# 倒叙删除
def delete_all_by_odd(list_target):
    for i in range(len(list_target)-1,-1,-1):
        if list_target[i]%2:
             del list_target[i]  #修改可变

# 传入可变
list01=[3,7,5,6,7,8,9,13]
delete_all_by_odd(list01)
print(list01)