"""
返回字符串中第一个不重复的字符
输入：ABCACDBEFD
输出：E
"""
str01="ABCACDBEFD"
for i in str01:
    if str01.count(i)==1:
        print(i)
        break

# def not_repead(str01):
#     for i in str01:
#         if str01.count(i) == 1:
#             return i
#
# res=not_repead("ABCACDBEFD")
# print(res)