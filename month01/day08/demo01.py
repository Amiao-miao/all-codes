"""
函数
    参数
"""
def add(number1,number2):
    result=number1+number2
    return result #返回数据

number1=int(input("请输入第一个数字："))
number2=int(input("请输入第二个数字："))
res=add(number1,number2)
print("结果是："+str(res))