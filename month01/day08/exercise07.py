"""
创建函数,根据年月计算天数.
        如果2月是闰年,则29天
        　　　 平年    28
month = int(input("请输入月份:"))
if 1 <= month <= 12:
    if month == 2:
        print("29天")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("30天")
    else:# 1 3 5 7 8 10 12
        print("31天")
else:
    print("月份有误")

year = int(input("请输入年份:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    day = 29
else:
    day = 28
"""
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def get_days(year,month):
    if month<1 or month>12:
        return "月份有误"
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    return 31

day=get_days(2020,2)
print(day )


