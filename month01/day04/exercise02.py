"""
在终端中累加 0  1  2  3
在终端中累加 2  3  4  5  6
在终端中累加 1  3  5  7
在终端中累加 8  7  6  5  4
在终端中累加 -1  -2  -3  -4  -5
"""
sum_num=0
for item in range(8,3,-1):
    sum_num+=item
print(sum_num)