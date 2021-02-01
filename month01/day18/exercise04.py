"""
为sum_data,增加打印函数执行时间的功能.
        函数执行时间公式： 执行后时间 - 执行前时间
def sum_data(n):
    sum_value = 0
    for number in range(n):
        sum_value += number
    return sum_value

print(sum_data(10))
print(sum_data(1000000))
"""
import time

def print_execute_time(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time=time.time()
        print(f"执行时间：,{start_time}-{stop_time}")
        return res  #执行旧功能
    return wrapper

@print_execute_time
def sum_data(n):
    sum_value = 0
    for number in range(n):
        sum_value += number
    return sum_value

print(sum_data(10))
print(sum_data(1000000))