"""
创建函数,计算梯形面积.
top_base = float(input("请输入上底："))
bottom_base = float(input("请输入下底："))
height = float(input("请输入高："))
result = (top_base + bottom_base) * height / 2
print("梯形面积是：" + str(result))
"""

def deciare(top_base,bottom_base,height):
    return (top_base + bottom_base) * height / 2
top_base = float(input("请输入上底："))
bottom_base = float(input("请输入下底："))
height = float(input("请输入高："))
res=deciare(top_base,bottom_base,height)
print(res)