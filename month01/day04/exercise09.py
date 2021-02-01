"""
 字符串： content = "我是京师监狱狱长金海"
    打印第一个字符、打印最后一个字符、打印中间字符
    打印字前三个符、打印后三个字符
    命题：金海在字符串content中
    命题：京师监狱不在字符串content中
    通过切片打印“京师监狱狱长”
    通过切片打印“长狱狱监师京”
    通过切片打印“我师狱海”
    倒序打印字符
"""
content = "我是京师监狱狱长金海。"
print(content[0])  #打印第一个字符
print(content[-1])  #打印最后一个字符
print(content[len(content)//2])  #打印中间字符
print(content[:3])   #打印字前三个符
print(content[-3:])   #打印后三个字符
print("金海" in content)  #命题：金海在字符串content中
print("京师监狱" not in content)  #命题：京师监狱不在字符串content中
print(content[2:-3])   #打印“京师监狱狱长
print(content[-4:1:-1])   #打印“长狱狱监师京
print(content[::3])   #打印“我师狱海
print(content[::-1])   #倒序打印字符