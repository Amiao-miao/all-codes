list01=[55,67,65,76,8,6,9,64]

for r in range(len(list01)-1):  #取数据
    for c in range(r+1,len(list01)): #作比较
        if list01[r]>list01[c]:     #如果发现更小
            list01[r],list01[c]=list01[c],list01[r]  #则交换
print(list01)