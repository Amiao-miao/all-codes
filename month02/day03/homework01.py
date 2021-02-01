"""
 编写一个程序，每隔2秒向文件 my.log中写入一行
     内容（如果这个文件不存在则自动创建）
     程序死循环不会停止. 当强行结束程序，重新启动之后
     能够继续写入内容，并序号衔接，每次写入一行都要显
     示出来

        1. 2020-11-30 18:18:18
        2. 2020-11-30 18:18:20
        3. 2020-11-30 18:18:22
        4. 2020-11-30 18:18:24
        5. 2020-11-30 18:20:08
        6. 2020-11-30 18:20:10
        7. 2020-11-30 18:20:12
"""
import time
file=open("my.log",'a+',buffering=1)
# count=1
file.seek(0,0) #文件偏移量在开头
count=len(file.readlines())+1
while True:
    tm=time.localtime()
    date="%d"%count+" . "+"%d-%d-%d %d:%d:%d\n"%tm[:6]
    file.write(date)
    count+=1
    time.sleep(2)



