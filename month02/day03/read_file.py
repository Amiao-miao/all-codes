"""
读取文件内容 示例
"""

#打开文件
filename="3.txt"
file=open(filename,"r")

#读取文件内容
# data=file.read(5)
# print(data)
# data=file.read()  #从上面字符结束读到结尾
# print(data)

#按行读取
# data=file.readline()
# print(data)
# data=file.readline(3)
# print(data)

#将文件内容读取为一个列表
# lines=file.readlines(4)  #参数也是读取整行
# print(lines)

#迭代获取
for line in file:
    print(line)

#关闭文件
file.close()