"""
在终端中录入5个人的身高，计算平均高度
在终端中录入多个人的身高，如果输入空字符串，则停止录入，再计算平均身高
"""
# sum_height=0
# for item in range(5):
#    sum_height+=int(input("请输入身高:"))
# print("平均身高："+str(sum_height/5))
# sum_height = 0
# count = 0
# while True:
#     height = input("请输入身高：")
#     if height == "":
#         break
#     sum_height += int(height)
#     count += 1
# print("平均身高：" + str(sum_height / count))
sum_value=0
for i in range(5):
    height=int(input(f"请输入第{i+1}个身高:"))
    if height=="":
        break
    sum_value+=height
print(sum_value/5)

