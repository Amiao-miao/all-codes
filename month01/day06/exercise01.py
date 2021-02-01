"""
    根据月日,计算是这一年的第几天.
    公式：前几个月总天数 + 当月天数
    例如：5月10日
    计算：31  29  31  30 + 10
"""
year=int(input("请输入年："))
month=int(input("输入月："))
day=int(input("输入日："))
day_of_month02=29 if year % 4 == 0  and year % 100 != 0 or year % 400 == 0 else 28
days_of_month=(31,29,31,30,31,30,31,31,30,31,30,31)
# result=0
# for i in range(month-1):
#     result+=days_of_month[i]
result=sum(days_of_month[:month-1])
result+=day
print(result)