"""
    使用闭包模拟以下情景：
    在银行开户存入10000
    购买xx商品花了xx元
    购买xx商品花了xx元
"""

def save_money(money):
    print("在银行开户存入%d"%money)

    def get_buy(commodity,price):
        nonlocal money
        money-=price
        print("购买%s商品花了%d元,还剩%d元"%(commodity,price,money))
    return get_buy

action=save_money(10000)
action("棉花糖",50)

