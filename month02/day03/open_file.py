"""
文件打开操作
"""

# 打开文件
# file=open("3.txt",'w')
# print(file)

#追加，文件内容不清空
file=open("3.txt",'a')
print(file)

#关闭文件
file.close()