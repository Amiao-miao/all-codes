"""在地区列表中删除“新疆”
在新增列表中删除第1个元素
在现有列表中删除前2个元素
"""
list_area=["香港","上海","新疆"]
list_increase=[15,6,0]
list_now=[393,61,49]

list_area.remove("新疆")
print(list_area)

del list_increase[0]
print(list_increase)

del list_now[:-2]
print(list_now)