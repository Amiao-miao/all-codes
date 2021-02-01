"""
 如果账号的密码错误3次，提示锁定账户，效果如下：
        请输入账号：qtx
        请输入密码：1234
        登录失败
        你还剩余 2 次机会
        请输入账号：Qtx
        请输入密码：1234
        登录失败
        你还剩余 1 次机会
        请输入账号：Qtx
        请输入密码：123456
        登录成功
"""
username="Qtx"
password="123456"

for i in range(3):
    name=input("请输入账户：")
    word=input("请输入密码：")

    if name==username:
        print("登录成功")
        break
    else:
        print("登录失败")
        print(f"你还剩余{2-i}次机会")
else:
    print("锁定账户")



# name="Qtx"
# word="123456"
# count=0
# item=4
# while count<3:
#     count+=1
#     item-=1
#     print("你还剩余%d次机会"%(item))
#     usename=input("请输入账号：")
#     password=input("请输入密码：")
#     if usename==name and password==word:
#         print("登录成功")
#         break
#     else:
#         print("登录失败")
# else:
#     print("锁定账户")

"""
 在终端中录入4个同学年龄,打印最小的年龄。
"""
# age01=int(input("请输入年龄："))
# age02=int(input("请输入年龄："))
# age03=int(input("请输入年龄："))
# age04=int(input("请输入年龄："))
# min_age=age01
# if min_age>age02:
#     min_age=age02
# if min_age>age03:
#     min_age=age03
# if min_age>age04:
#     min_age=age04
# print("年龄最小的是%d"%(min_age))




