"""
不改变插入函数与删除函数代码，为其增加验证权限的功能
def verify_permissions(func):
    print("验证权限")
def insert():
    print("插入")
def delete():
    print("删除")

insert()
delete()
"""
def verify_permissions(func):
    def new_func(*args,**kwargs):
        print("验证权限")
        res=func(*args,**kwargs)
        return res
    return new_func
# insert=verify_permissions(insert)

@verify_permissions
def insert():
    print("插入")
    return True

@verify_permissions
def delete(p1):
    print("删除",p1)
    return False

print(insert())
print(delete(10))