"""
文件偏移量
"""

file=open("3.txt",'wb+')

file.write("2020-11-三十".encode())
file.flush()
# file.tell(),查看偏移量
print("文件偏移量：",file.tell())

#设置文件偏移量
file.seek(-2,2)
file.write(b"28")

# date=file.read()
# print(date)

file.close()