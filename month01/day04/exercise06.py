"""
在终端中录入一个内容,循环打印每个文字的编码值。
效果：
请输入文字：qtx
113
116
120
"""
#
# num=input("请输入文字：")
# for item in num:
#     print(ord(item))


"""
循环录入编码值打印文字，直到输入空字符串停止。
	效果：
请输入数字：113
q
请输入数字：116
t
请输入数字： 
Process finished with exit code 0
"""

while True:
    num=input("请输入数字：")
    if num=="":
        break
    print(chr(int(num)))
