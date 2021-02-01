"""
练习：
    在终端中,循环录入字符串,如果录入空则停止.
    停止录入后打印所有内容(一个字符串)
"""

list_result=[]
while True:
    num=input("请输入字符：")
    if num=="":
        break
    else:
        list_result.append(num)
str_result="".join(list_result)
print(str_result)