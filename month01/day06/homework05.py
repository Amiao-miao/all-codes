"""
    将列表中所有元素转换为一个字符串
    列表:["我", "爱", "你", "p", "y", "t", "h", "o", "n", 666]
    结果:我爱你python666
  注意：列表中包含非字符串数据
"""

list01=["我", "爱", "你", "p", "y", "t", "h", "o", "n", 666]
list02=[]
for item in list01:
    list02.append(str(item))
result = "".join(list02)
print(result)

# result="".join([str(item) for item in list01])
# print(result)