"""
僵尸进程演示
* join 在阻塞等待子进程，子进程退出时会清理僵尸
* 每次start前会自动清理已经产生的僵尸
"""
from multiprocessing import Process
from time import sleep
import os
from signal import *

#断绝父子关系，从此子进程退出与父进程无关
#忽略子进程退出行为
signal(SIGCHLD,SIG_IGN)

def fun():
    print("开始运行一个进程:",os.getpid())
    sleep(2)
    print("终于完成事情结束喽")

p=Process(target=fun)
p.start()
p.join()
while True:
    pass

