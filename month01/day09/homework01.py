list_commodity_infos = [
    {"cid": 1001, "name": "屠龙刀", "price": 10000},
    {"cid": 1002, "name": "倚天剑", "price": 10000},
    {"cid": 1003, "name": "金箍棒", "price": 52100},
    {"cid": 1004, "name": "口罩", "price": 20},
    {"cid": 1005, "name": "酒精", "price": 30},
]
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]


def print_sigle_order(i):
    print("商品编号%d, 商品名称%s, 商品单价%d."%(i["cid"],i["name"],i["price"]))

# 定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
def print_all_order():
    for i in list_commodity_infos:
        print_sigle_order(i)
print_all_order()

# 定义函数,打印商品单价小于2万的商品信息
def print_get_2w_order():
    for i in list_commodity_infos:
        if i["price"]<20000:
            print_sigle_order(i)
print_get_2w_order()

# 定义函数,打印所有订单中的商品信息,
# 格式：商品名称xx,商品单价:xx,数量xx.
def print_all_orders():
    for order in list_orders:
        for commodity in list_commodity_infos:
            if order["cid"]==commodity["cid"]:
                print("商品名称%s,商品单价%d,数量%d"%(commodity["name"],commodity["price"],order["count"]))
                break
print_all_orders()

# (4) 定义函数,在商品列表中查找最贵的商品
def gt_max_order():
    max_value=list_commodity_infos[0]
    for ii in range(1,len(list_commodity_infos)):
        if max_value["price"]<list_commodity_infos[ii]["price"]:
            max_value=list_commodity_infos[ii]
    return max_value
print(gt_max_order())

# (5) 定义函数,根据单价对商品列表升序排列
def ascending_commodity_by_price():
    for r in range(len(list_commodity_infos)-1):
        for c in range(r+1,len(list_commodity_infos)):
            if list_commodity_infos[r]["price"]>list_commodity_infos[c]["price"]:
                list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[r]
ascending_commodity_by_price()
print(list_commodity_infos)

# (6)定义函数, 删除单价大于5000的商品
def print_delete_5000_order():
    for items in range(len(list_commodity_infos)-1,-1,-1):
        if list_commodity_infos[items]["price"]>5000:
            del list_commodity_infos[items]

print_delete_5000_order()
print(list_commodity_infos)






