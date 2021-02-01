"""
数据库写操作示例2
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
stu_list=[
    ("张三",18,'m',98),
    ("李四",17,'w',94),
    ("王五",16,'m',96)
]
try:
    sql="insert into cls(name,age,sex,score) values (%s,%s,%s,%s);"
    cur.executemany(sql,stu_list)
    db.commit()#提交写操作
except Exception as e:
    print(e)
    db.rollback()#回滚

#关闭数据库连接
cur.close()
db.close()