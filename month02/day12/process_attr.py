from multiprocessing import Process
from time import sleep


def fun():
    print("开始运行一个进程喽")
    sleep(2)
    print("终于完成事情结束喽")

p=Process(target=fun,name="Aid",daemon=True)
p.start()
print(p.name)  #进程名称
print(p.pid)   #对应子进程的PID号
print(p.is_alive())  #查看子进程是否在生命周期
