"""
练习1：
需求：
    定义函数，在列表中查找奇数
    定义函数，在列表中查找能被3或5整除的数字
"""
list01 = [63, 5, 56, 7, 8, 9]
def find01(number):
    return number%2!=0

def find02(number):
    return number%3==0 or number%5==0

def find_all(func):
    for number in list01:
        if func(number):
            yield number

for item in find_all(find02):
    print(item)