"""
请在屏幕上使用input函数输入一首古诗
《悯农》
将其写入到文件file.txt中
要求每次input只输入一句
"""

file=open("file.txt",'w')
while True:
    data=str(input("请输入古诗："))
    if not data:
        break
    file.writelines(data+"\n")

file.close()
