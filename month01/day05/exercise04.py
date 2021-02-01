list_planet=["水星" ,"金星" ,"火星" ,"木星"] #创建列表存储4个行星：“水星” "金星" "火星" "木星"
print(list_planet)

list_planet.insert(2,"地球")
print(list_planet)
list_planet.append("土星")
list_planet.append("天王星")
list_planet.append("海王星")
print(list_planet)

print(list_planet[0])
print(list_planet[-1])

print(list_planet[:2])

list_planet.remove("海王星")
print(list_planet)
del list_planet[3]
print(list_planet)