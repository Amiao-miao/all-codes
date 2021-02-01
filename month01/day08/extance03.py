"""
判断二维列表是否存在某个数字
"""
# list01=[[1,2,3],[4,5,6],[7,8,9]]
# number=11
# for i in list01:
#     if number in i:
#         print(True)
#         break
# else:
#     print(False)
#

def is_in(list01,number):
    """

    :param list01: 二维列表
    :param number:
    :return:
    """
    for i in list01:
        if number in i:
            return True
    else:
        return False

res=is_in([[1,2,3],[4,5,6],[7,8,9]],11)
print(res)