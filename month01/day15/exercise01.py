import module_exercise01

print(module_exercise01.data)
module_exercise01.func01()

my=module_exercise01.MyClass()
my.func02()

module_exercise01.MyClass.func03()


from module_exercise01 import *
print(data)
func01()
m=MyClass()
m.func02()
MyClass.func03()