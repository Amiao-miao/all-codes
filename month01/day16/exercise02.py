"""
	练习1：创建列表,使用迭代思想,打印每个元素.
"""

list01=[1,2,3,4]
iterator=list01.__iter__()
while True:
    try:
        item=iterator.__next__()
        print(item)
    except StopIteration:
        break