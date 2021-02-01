"""
假设在当前文件夹下有一个图片timg.jpeg
请编写一个函数，将该文件名传入，通过执行函数将其
复制一份到主目录下
注意：考虑可能文件比较大，不允许一次性读取
"""
def get_pic(filename):
    fr=open(filename,'rb')  #原文件
    fw=open("/home/tarena/"+filename,'wb')

    #边读边写
    while True:
        data=fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

get_pic("timg.jpg")


