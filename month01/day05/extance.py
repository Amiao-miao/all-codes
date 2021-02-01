"""
输入三个整数x,y,z,请把这三个数由小到大输出一个列表
"""
res=[]
x=int(input("请输入整数："))
y=int(input("请输入整数："))
z=int(input("请输入整数："))

#x是最小值
if x>y:
    x,y=y,x #交换值，x变为小的值
if x>z:
    x,z=z,x  #x交换成最小值
if y>z:
    y,z=z,y
#x<y<z
res.append(x)
res.append(y)
res.append(z)
print(res)
