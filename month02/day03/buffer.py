
#行缓冲打开
file=open("3.txt",'wb',buffering=10)

while True:
    data=input("<<")
    if not data:
        break
    file.write((data+"\n").encode())


    # file.flush()  #刷新缓冲
file.close()