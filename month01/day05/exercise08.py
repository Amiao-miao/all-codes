"""
生成10--30之间能被3或者5整除的数字
[10, 12, 15, 18, 20, 21, 24, 25, 27]
生成5 -- 20之间的数字平方
[25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
"""
# list01=[]
# for item in range(10,31):
#     if item%3==0 or item%5==0:
#         list01.append(item)
#         print(list01)

list01=[item for item in range(10,31) if item%3==0 or item%5==0]
print(list01)

list02=[num**2 for num in range(5,21)]
print(list02)



