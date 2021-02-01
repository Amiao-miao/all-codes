"""
编写一个程序，输入一个学生的姓名，将该学生成绩改为100分
"""
import pymysql

args={
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"stu",
    "charset":"utf8"
}

#连接数据库
db=pymysql.connect(**args)

#创建游标 游标对象：执行sql得到执行结果的对象
cur = db.cursor()

#数据写操作 insert delete update
try:
    name=input("Name:")
    sql=f"update cls set score=100 where name='{name}';"
    cur.execute(sql)
    db.commit()#提交写操作
except Exception as e:
    print(e)
    db.rollback()#回滚

#关闭数据库连接
cur.close()
db.close()