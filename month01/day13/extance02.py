"""
    定义函数，根据输入的字符串（只有字母与数字），分别统计出其中英文字母
    数字的个数
"""

def get_number(target_str):
    """
    gets the number of digits and letters in the target string
    :param target_str:  type:str
    :return:
    """

    number_res=0
    abc_res=0
    for i in target_str:
        if i.ispnumeric():   #计算数字的数量
            number_res+=1

        if i.isalpha():    #计算字母的数量
            abc_res+=1
        return  number_res,abc_res

s="hakhbd321"
number_res,abc_res=get_number(s)
print("数字的数量为",number_res)
print("字母的数量为",abc_res)