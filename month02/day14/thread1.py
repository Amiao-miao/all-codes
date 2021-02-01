"""
线程基础示例1
"""
import threading
from time import sleep
import os
a=1
#线程执行函数
def music():

    for i in range(3):
        sleep(2)
        global a
        print(a)
        a=1000
        print(os.getpid(),"播放：水瓶")


#实例化线程对象
t=threading.Thread(target=music)
#启动线程
t.start()

for i in range(4):
    sleep(1)
    print(os.getpid(),"播放：云与海")

print(a)
#阻塞等待线程结束
t.join()