"""
  在终端中录入4个同学身高,打印最高的值.
    算法：
        170    160    180    165
        假设第一个就是最大值
        使用假设的和第二个进行比较, 发现更大的就替换假设的
        使用假设的和第三个进行比较, 发现更大的就替换假设的
        使用假设的和第四个进行比较, 发现更大的就替换假设的
        最后，假设的就是最大的.
	效果：
请输入第1个同学身高:170
请输入第2个同学身高:160
请输入第3个同学身高:180
请输入第4个同学身高:165
最高的同学:180
"""
# stature01 = int(input("请输入第1个同学的身高："))
# stature02 = int(input("请输入第2个同学的身高："))
# stature03 = int(input("请输入第3个同学的身高："))
# stature04 = int(input("请输入第4个同学的身高："))
# max_value = stature01
# if max_value < stature02:
#     max_value = stature02
# if max_value < stature03:
#     max_value = stature03
# if max_value < stature04:
#     max_value = stature04
# print("最高的同学：" + str(max_value))
list01=[]
for i in range(4):
    result=int(input(f"请输入第{i+1}个同学的身高："))
    list01.append(result)
max_value=list01[0]
for item in range(1,len(list01)):
    if max_value<list01[item]:
        max_value=list01[item]
print(max_value)


