"""
在终端中获取一个整数，作为边长，打印矩形。
效果：
	请输入整数:5
*****
*   *
*   *
*   *
*****
"""

number=int(input("请输入整数："))
for item in range(number):
    if item==0 or item==number-1:
        print(number*"*")
    else:
        print("*%s*"%(" "*(number-2)))








# num=int(input("请输入整数："))
# for count in range(num):
#     if count==0 or count==num-1:
#         print("*" * num)
#     else:
#         print("*%s*"%(" "*(num-2)))


