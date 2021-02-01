"""
列表推导式：
  计算1970年到2050年之间所有闰年
"""

list_year=[]
for i in range(1970,2051):
    if i% 4 == 0  and i% 100 != 0 or i% 400 == 0:
        list_year.append(i)
print(list_year)

