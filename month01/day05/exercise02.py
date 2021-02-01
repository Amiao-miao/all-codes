"""
   打印香港疫情信息(xx地区新增xx人现存xx人)
        将地区列表后2个元素修改为 ["XJ","SC"]
        打印地区列表元素(一行一个)
        倒序打印新增列表元素(一行一个)
"""

list_area=["香港","上海","新疆"]
list_increase=[15,6,0]
list_now=[393,61,49]
#打印香港疫情信息(xx地区新增xx人现存xx人)
#print(f"{list_area[0]}地区新增{list_increase[0]}人现存{list_now[0]}人")
#将地区列表后2个元素修改为 ["XJ","SC"]
list_area[-2:]=["XJ","SC"]
print(list_area)
#打印地区列表元素(一行一个)
#for item in list_area:
  #  print(item)
#倒序打印新增列表元素(一行一个)
#for i in range(len(list_area)-1,-1,-1):
 #   print(list_area[i])