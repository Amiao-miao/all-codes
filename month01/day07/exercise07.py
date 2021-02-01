"""
对数字列表进行降序排列（大 --> 小）
"""

list01=[55,67,65,76,8,6,9,64]

for x in range(len(list01)-1):
    for y in range(x+1,len(list01)):
        if list01[x]<list01[y]:
            list01[x],list01[y]=list01[y],list01[x]
print(list01)