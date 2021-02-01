"""
文件写方法 示例
"""
#打开一个文件
file=open("3.txt",'w')


#写入内容
# file.write("hello,来了\n".encode())
# n=file.write("干啥\n".encode())
# print("写入 %d 字节"%n)

data=[
    "先帝创业未半\n",
    "而中道崩殂\n"
]
file.writelines(data)

#关闭
file.close()