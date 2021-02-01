"""
多线程创建
"""

from threading import Thread
from time import sleep

def fun(sec,name):
    print("含有参数的线程来喽")
    sleep(sec)
    print(f"{name}线程执行完成啦")

#创建多个线程
jobs=[]
for i in range(5):
    t=Thread(target=fun,args=(2,f"T-{i}"))
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()
