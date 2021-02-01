# """
# 请输入商品单价：5
# 请输入购买数量：3
# 请输入支付金额：20
# 应找回：5.0
# """
# price=float(input("请输入商品单价："))
# count=int(input("请输入商品数量："))
# amount=float(input("请输入商品支付金额："))
# result=amount-price*count
# print("应找回："+str(result))


# """
# 在终端中输入一个疫情确诊人数再录入一个治愈人数，打印治愈比例
# 格式：治愈比例为xx%
# 效果：
# 请输入确诊人数：500
# 请输入治愈人数：495
# 治愈比例为99.0%
# """
# count_quezhen=int(input("请输入确诊人数："))
# count_zhiyu=int(input("请输入治愈人数："))
# result=count_zhiyu/count_quezhen*100
# print("治愈比例为"+str(result)+"%")


# """
# 古代的秤，一斤十六两。在终端中获取两，计算几斤零几两。
# 效果：
# 请输入总两数：100
# 结果为：6斤4两
# """
#
# weight=int(input("请输入总两数："))
# jin=weight//16
# liang=weight%16
# print("结果为："+str(jin)+"斤"+str(liang)+"两")

"""
在终端中输入一个四位整数，计算每位相加和。
例如：录入1234，打印1+2+3+4结果
效果：
请输入四位整数：1234
结果是：10
"""

# number=int(input("请输入四位整数："))
# num01=number//1000
# num02=number//100%10
# num03=number//10%10
# num04=number%10
# result=num01+num02+num03+num04
# print("结果是："+str(result))

"""
根据命题写出代码
输入的是正数
输入的是月份
输入的不是偶数
"""
print(int(input("输入数字:"))>=0)
print(1<=int(input("输入月份:"))<=12)
print(int(input("输入数字:"))%2!=0)
