"""
字节串使用示例
*所有字符串都能转换为字节串
*不是所有字节串都能转换为字符串
"""

#定义一个字节串变量
b=b"hello world"  # 只能用于ASCII字符
print(type(b))

#定义非ASCII字节串变量
b1="您好".encode()
print(b1)
# 对于一个变量,将字符串改变为字节串也用encode

s1=b1.decode()
print(s1)
# decode将字节串转换为字符串
