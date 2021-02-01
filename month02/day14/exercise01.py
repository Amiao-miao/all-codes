"""
现在有500车票  记为T1--T500
共有10个窗口同时买票  W1--W10

编写一个程序模拟买票过程
卖出一张票则打印 W1--T200
卖出后隔0.1秒才能出下一张
卖空为止
"""

from threading import Thread,Lock
from time import sleep

lock=Lock()
#将车票准备好
list_ticket=[]
for i in range(1,501):
    list_ticket.append(f"T{i}")
#ticket=["T%d" %x for x in range(1,501)]

def sale(w):
    while list_ticket:

        print(f"{w}---{list_ticket[0]}")
        del list_ticket[0]
        sleep(0.1)



#创建10个线程

jobs=[]
for i in range(1,11):

    t = Thread(target=sale, args=(f"W{i}",))
    jobs.append(t)
    t.start()

[i.join() for i in jobs]
