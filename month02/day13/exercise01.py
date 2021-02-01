"""
拷贝一个目录
假设目录下有若干普通文件，需要编写程序
将该目录拷贝一份，注意拷贝过程中需要
多文件同时拷贝（使用进程池完成）
"""

from multiprocessing import Pool
import os


#进程池事件 将文件从原文件夹拷贝到新文件夹
def copy(filename,old,new):
    fr=open(old+'/'+filename,'rb')
    fw=open(new+'/'+filename,'wb')
    while True:
        data=fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

#创建进程池，调用函数作为进程池执行事件
def main(old_folder):
    #创建新文件夹
    new_folder=old_folder.split("/")[-1]
    os.mkdir(new_folder)
    #获取文件里列表
    file_list=os.listdir(old_folder)

    pool=Pool()

    for file in file_list:
        pool.apply_async(copy,args=(file,old_folder,new_folder))
    pool.close()
    pool.join()

if __name__ == '__main__':
    main("/home/tarena/FTP")




