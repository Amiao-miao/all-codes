"""
进程池示例
"""

from multiprocessing import Pool
from time import *
from random import random


#进程池事件
def worker(msg,sec):
    sleep(sec)  # 每次处理订单的时间
    print(ctime(),"---",msg)

#创建进程池
pool=Pool(4)

#将事件加入到进程池执行等待队列中
for i in range(1,21):
    msg="订单-%d"%i
    pool.apply_async(worker,args=(msg,random()*3))

pool.close() #关闭
pool.join()  #阻塞等待进程池运行结束
