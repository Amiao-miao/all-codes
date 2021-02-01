"""
根据下列文字，提取变量，使用字符串格式化打印信息
湖北确诊67802人,治愈63326人,治愈率0.99
70秒是01分零10秒
"""
# province=input("请输入省份：")
# num_diagnose=int(input("请输入确诊人数："))
# num_cure=int(input("请输入治愈人数："))
# probability=num_cure/num_diagnose
# print("%s确诊%d人，治愈%d人，治愈率%.2f"%(province,num_diagnose,num_cure,probability))

total=70
print("%d是%.2d分零%.2d秒"%(total,total//60,total%60))