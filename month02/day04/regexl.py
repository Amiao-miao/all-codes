"""
re 模块使用
"""
import re

s = "学生信息：Alex:1996,Sunny:1998"
pattern = r"(\w+):(\d+)"
#如果正则表达式中有组，那么只能得到组所对应的
# result = re.findall(pattern, s)
# print(result)
#
result=re.split("\W",s)
print(result)


# print(re.sub(r"\W", "##", s))