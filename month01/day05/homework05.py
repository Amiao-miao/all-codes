"""
    在终端中录入5个疫情省份的确诊人数
   最后打印最大值、最小值、平均值.
"""
res=[]
for i in range(5):
    num=int(input(f"请输入第{i+1}个确诊人数："))
    res.append(num)
print(max(res))
print(min(res))
print(sum(res)/len(res))



