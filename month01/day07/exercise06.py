"""
骰子（1～6）
排列出两个骰子可以组成的所有可能
    三个
"""

list_result=[]
for num1 in range(1,7):
    for num2 in range(1,7):
        for num3 in range(1, 7):
            list_result.append((num1,num2,num3))
print(list_result)

# list_result=[(num1,num2) for num1 in range(1,7) for num2 in range(1,7)]
# print(list_result)