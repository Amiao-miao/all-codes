from threading import Lock,Thread,Event

# lock=Lock()
e=Event()
a=b=1

def fun():
    while True:
        # lock.acquire()
        if a!=b:
            print(f"a={a},b={b}")
        e.set()
        # lock.release()
t=Thread(target=fun)
t.start()

while True:
    # lock.acquire()
    e.wait()
    a+=1
    b+=1
    # lock.release()

t.join()