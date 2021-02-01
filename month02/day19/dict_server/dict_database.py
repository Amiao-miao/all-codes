"""
数据库的交互处理
"""
import pymysql

class Database:
    args={
        "host":"localhost",
        "port":3306,
        "user":"root",
        "password":"123456",
        "database":"dict",
        "charset":"utf8"
    }
    def __init__(self):
        self.db = pymysql.connect(**Database.args)

    def course(self):
        self.cur =self.db.cursor()

    def close(self):
        self.db.close()

    def register(self,name,passwd):
        sql="insert into user (name,psaawd) values (%s,%s)"
        try:
            self.cur.execute(sql,[name,passwd])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    def login(self,name,passwd):
        sql="select name from user where name=%s and passwd=%s"
        self.cur.execute(sql,[name,passwd])
        if self.cur.fetchone():
            return True
        else:
            return False

    def query(self,word):
        sql="select mean from words where word=%s"
        self.cur.execute(sql,[word])
        mean=self.cur.fetchone()
        if mean:
            return True
        else:
            return False

    def hist(self,name,word):
        pass