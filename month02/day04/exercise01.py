"""
编写一个程序，删除主文目录下 下载文件夹中
大小小于1kb的文件
"""
#
# import os
# list01=os.listdir("/home/tarena/下载")
#
# for item in list01:
#     size =os.path.getsize("/home/tarena/下载/"+item)
#     if size < 1024 and os.path.isfile("/home/tarena/下载/"+item):
#         os.remove("/home/tarena/下载/"+item)

import os
dir="/home/tarena/下载/"

for file in os.listdir(dir):
    filename=dir+file
    if os.path.getsize(filename)<1024 and os.path.isfile(filename):
        os.remove(filename)


