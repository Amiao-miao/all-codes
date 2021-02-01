"""
正则表达式
"""
import re
#目标字符串
s="""Hello
北京
"""
#让^ $ 表示每一行的开头结尾位置
result=re.findall(r"^\w+",s,re.M)
print(result)

#让 . 可以匹配换行
# result=re.findall(r".+",s,re.S)
# print(result)

#忽略字母大小写
# result=re.findall(r"[a-z]+",s,re.I)
# print(result)

#只匹配ASCII字符
# result=re.findall(r"\w+",s,re.A)
# print(result)