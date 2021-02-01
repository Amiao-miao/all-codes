"""
list01 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]
1. 将第一行从左到右逐行打印
2. 将第二行从右到左逐行打印
3. 将第三列行从上到下逐个打印
4. 将第四列行从下到上逐个打
5. 将二维列表以表格状打印
"""

list01 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]
#将第一行从左到右逐行打印
for item in list01[0]:
    print(item)
#将第二行从右到左逐行打印
for r in range(len(list01[1]) - 1, -1, -1):
    print(list01[1][r])
#将第三列行从上到下逐个打印
for c in range(len(list01)):
    print(list01[c][2])
#将第四列行从下到上逐个打印
for a in range(len(list01)-1,-1,-1):
    print(list01[a][3])
#将二维列表以表格状打印
for b in range(len(list01)):
    for d in range(len(list01[b])):
        print(list01[b][d],end="\t")
    print()


