"""
进程间通信示例
"""
from multiprocessing import Process,Queue

q=Queue()
def handle():
    while True:
        res=q.get()
        try:
            #将res作为语句执行
            eval(res)
        except:
            print("语法有误")

p=Process(target=handle,daemon=True)
p.start()

while True:
    res=input("请输入语句:")
    if res=="exit":
        break
    q.put(res)