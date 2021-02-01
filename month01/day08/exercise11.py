# ---------全局变量--------
# 商品字典
dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}
# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]
# ---------函数--------
# 1.定义函数,打印所有商品信息
# 格式：商品编号xx,商品名称xx,商品单价xx.
def print_commodity_all():
    for k,v in dict_commodity_infos.items():
        print("商品编号%d,商品名称%s,商品单价%d."%
              (k,v["name"],v["price"]))
print_commodity_all()
# 2.定义函数,打印所有订单中的信息,
# 格式：商品编号xx,购买数量xx.
