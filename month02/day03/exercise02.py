"""
单词本：每行一个单词
       单词和解释之间有空格
       后面的单词比前面的大
编写一个函数，传入一个单词
返回单词的对应解释
"""

def find_word(word:str)->str:
    """
    :param word: 要查找的单词
    :return: 得到的解释
    """
    file=open("dict.txt")
    for line in file:
        tmp=line.split(" ",1)  #按照空格分割,1表示只切割一次
        if tmp[0]>word:
            break
        elif word==tmp[0]:
            file.close()
            return tmp[1].strip()  #去除字符串两侧的空格
        file.close()

print(find_word("one"))