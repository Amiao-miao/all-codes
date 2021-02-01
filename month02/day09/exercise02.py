"""
创建数据库 dict
在其中创建一个数据表 words
id word mean

编写一个程序将dict.txt文本的单词存入该数据表
"""
import re

import pymysql

args={
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"dict",
    "charset":"utf8"
}


#数据写操作 insert delete update

def get_data(filename):
    """

    :param filename:  单词本文件
    :return:  可插入数据
    """
    data=[]
    file=open(filename,'r')
    for line in file:
        word=re.findall(r"(\w+)\s+(.*)",line)
        # tmp = line.split(" ", 1)# 按照空格分割,1表示只切割一次
        # word=tmp[0]
        # mean=tmp[1]
        # item=(word,mean)
        data.append(word[0])
    file.close()
    return data
def main():
    db = pymysql.connect(**args)
    cur = db.cursor()
    data=get_data("dict.txt")
    try:
        sql="insert into words(word,mean) values (%s,%s);"
        cur.executemany(sql,data)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

#关闭数据库连接
    cur.close()
    db.close()

if __name__=='__main__':
    main()