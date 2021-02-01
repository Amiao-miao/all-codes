"""
抢红包外挂：
外挂一：直接交5元，每次抢的钱超过10元，再交1元
外挂二：每次抢的钱超过5元，交1元
"""
cost_01 = 5
cost_02 = 0
while True:
    money=float(input("请输入每次抢的金额："))
    if money=="" or money=="exit":
        break

    if money>10:
        cost_01+=1
    if money>5:
        cost_02+=1

if cost_02>cost_01:
    print("第一种外挂花费："+str(cost_01))
    print("第二种外挂花费："+str(cost_02))
    print("第一种外挂更划算")
elif cost_02 < cost_01:
    print("第一种外挂花费：" + str(cost_01))
    print("第二种外挂花费：" + str(cost_02))
    print("第二种外挂更划算")
else:
    print("第一种外挂花费：" + str(cost_01))
    print("第二种外挂花费：" + str(cost_02))
    print("两种外挂花费相同")