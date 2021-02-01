"""
练习：累加10 -- 60之间，个位不是3/5/8的整数和。
思路：是3/5/8跳过，否则累加
"""
sum_item=0
for item in range(10,61):
    if item%10==3 or item%10==5 or item%10==8:
        continue
    sum_item+=item
print(sum_item)
