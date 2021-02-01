"""
质数：大于1的整数，除了1和它本身以外不能再被其他数字整除
获取指定范围内的所有质数
"""


# list01=[]
# start=input("请输入初始值：")
# stop=input("请输入结束值：")
# for number in range(start,stop+1):
#     for i in range(2,number):
#     if number%i==0:
#         break
# else:
#     list01.append(number)

def is_zhishu(number):
    for i in range(2,number):
        if number%i==0:
            return False
        return True

def find_zhishu(start,stop):
    res=[]
    for i in range(start, stop + 1):
        if is_zhishu(i):
            res.append(i)