"""
请输入商品单价：5
请输入购买数量：3
请输入支付金额：20
应找回：5.0
"""
price=float(input("请输入商品的单价："))
number=int(input("请输入商品的数量："))
payment=float(input("请输入商品的支付金额："))
get_back=payment-price*number
print("应找回:"+str(get_back))