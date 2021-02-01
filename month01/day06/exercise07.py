"""
    将两个列表，合并为一个字典
	姓名列表["张无忌","赵敏","周芷若"]
	房间列表[101,102,103]
    {101: '张无忌', 102: '赵敏', 103: '周芷若'}
"""

name=["张无忌","赵敏","周芷若"]
room=[101,102,103]
# dict01={}
# for i in range(len(name)):
#     key=room[i]
#     value=name[i]
#     dict01[key]=value
# print(dict01)

dict02={room[i]:name[i] for i in range(len(name))}
print(dict02)

# 颠倒练习1字典键值
dict03={v:k for k,v in dict02.items()}
print(dict03)