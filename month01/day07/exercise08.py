dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]
# 1.打印所有商品信息,
# 格式：商品编号xx,商品名称xx,商品单价xx.
for k,v in dict_commodity_infos.items():
    print("商品编号%d,商品名称%s,商品单价%d."%
          (k,v["name"],v["price"]))
# 2.打印所有订单中的信息,
# 格式：商品编号xx,购买数量xx.
for item in list_orders:
    print("商品编号%d,购买数量%d"%(item["cid"],item["count"]))
# 3.打印所有订单中的商品信息,
# 格式：商品名称xx,商品单价:xx,数量xx.
for i in list_orders:
    cid=i["cid"]
    commodity=dict_commodity_infos[cid]
    print("商品名称%s,商品单价%d,数量%d."%(commodity["name"],commodity["price"],i["count"]))
# 4.查找数量最多的订单(使用自定义算法,不使用内置函数)
max_value=list_orders[0]
for x in range(1,len(list_orders)):
        if max_value["count"]<list_orders[x]["count"]:
            max_value = list_orders[x]
print(max_value)
# 5. 根据购买数量对订单列表降序(大->小)排列
for a in range(len(list_orders)-1):
    for b in range(a+1,len(list_orders)):
        if list_orders[a]["count"]<list_orders[b]["count"]:
            list_orders[a],list_orders[b]=list_orders[b],list_orders[a]
print(list_orders)


