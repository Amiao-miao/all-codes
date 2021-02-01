"""
    在终端中录入疫情地区名称，如果输入空字符串，则停止。
   最后倒序打印所有地区名称(一行一个)
   要求：录入的名称已经存在不要再次添加.
   提示： in
"""
res=[]
while True:
    area=input("请输入疫情地区：")
    if area=="":
        break
    if area in res:
        print("已经存在")
    else:
        res.append(area)
for i in range(len(res)-1,-1,-1):
    print(i)
