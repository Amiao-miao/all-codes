"""
在练习1的基础上完成
在拷贝过程中不断显示拷贝的百分比

百分比=已经拷贝/总大小*100%
总大小=所有文件的大小之和
"""
from multiprocessing import Pool,Queue
import os

# 生成消息队列
q=Queue()

#进程池事件 将文件从原文件夹拷贝到新文件夹
def copy(filename,old,new):
    fr=open(old+'/'+filename,'rb')
    fw=open(new+'/'+filename,'wb')
    while True:
        data=fr.read(1024)
        if not data:
            break
        n=fw.write(data)
        q.put(n)  #将已经拷贝的大小给父进程
    fr.close()
    fw.close()

#获取文件大小
def total_size(dir):
    res=0
    for file in os.listdir(dir):
        res+=os.path.getsize(dir+'/'+file)
    return res


#创建进程池，调用函数作为进程池执行事件
def main(old_folder):
    #创建新文件夹
    new_folder=old_folder.split("/")[-1]
    os.mkdir(new_folder)
    #获取文件里列表
    file_list=os.listdir(old_folder)
    size=total_size(old_folder)
    pool=Pool()

    for file in file_list:
        pool.apply_async(copy,args=(file,old_folder,new_folder))

    pool.close()

    #求拷贝的百分比
    copy_size=0
    while copy_size<size:
        copy_size+=q.get()  #累加
        print("已拷贝%.2f%%"%(copy_size/size*100))

    pool.join()

if __name__ == '__main__':
    main("/home/tarena/FTP")
