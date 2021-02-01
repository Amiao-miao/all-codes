"""
包含参数的进程函数
"""

from multiprocessing import Process
from time import sleep


def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I am %s"%name)
        print("I am working")

p=Process(target=worker,
          args=(2,),
          kwargs={"name":"Tom"})  #元组字典传参

          # kwargs={"sec":2,"name":"Tom"}  #字典传参
          # args=(2,"Tom")  #元组传参

p.start()

p.join()
