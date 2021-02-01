""" 电梯设置规定：
            如果承载⼈不超过10⼈，且总重量不超过1000千克，可以正常使⽤，否则提示超载。
        步骤:
            终端中获取人数/总重量
            显示电梯正常运行
                电梯超载
"""
# number=int(input("请输入人数："))
# weight=float(input("请输入重量："))
# if number<=10 and weight<=1000:
#     print("正常运行")
# else:
#     print("电梯超载")

"""
根据年龄，输出对应的人生阶段。
            年龄       ⼈⽣阶段
            0-6 岁      童年
            7-17 岁     少年
            18-40 岁    ⻘年
            41-65 岁    中年
            65 岁之后    ⽼年
        步骤:
            终端中获取年龄
            显示人生阶段
"""
# age=int(input("请输入年龄："))
# if age<=6:
#     print("童年")
# elif age<=17:    程序能运行到本行，说明age一定大于6
#     print("少年")
# elif age<=40:
#     print("青年")
# elif age<=65:
#     print("中年")
# else:
#     print("老年")

"""
如果是vip客户,消费小于等于500,享受85折
            消费大于500,享受8折
如果不是vip客户,消费大于等于800,享受9折
            消费小于800,原价
在终端中输入账户类型,消费金额,计算折扣.
"""
# type_zhanghu=input("请输入账户类型：")
# money=float(input("请输入消费金额："))
# if type_zhanghu=="vip":
#     if money<=500:
#         print(money*0.85)
#     else:
#         print(money*0.8)
# else:
#     if money>=800:
#         print(money*0.9)
#     else:
#         print(money)

"""
在终端中累加 0  1  2  3
        在终端中累加 2  3  4  5  6
        在终端中累加 1  3  5  7
        在终端中累加 8  7  6  5  4
        在终端中累加 -1  -2  -3  -4  -5
"""
result=1
count=1
while count<8:
      result*=count
      count+=2
print(result)

