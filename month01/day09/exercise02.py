"""
    定义数值累乘的函数
"""

def get_numerical_value(*args):
    result=1
    for i in args:
        result*=i
    return result

res=get_numerical_value(1,2,3)
print(res)

