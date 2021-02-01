"""
斐波那契数列
[1,1,2,3,5,8,13…]
"""
long=int(input("请输入斐波那契数列的长度："))
if long==1:
    print([1])
elif long==2:
    print([1,1])
else:
    res=[1,1]                                     # res=[1,1]
    for i in range(long-2):                       # a3=res[0]+res[1]
       a3=res[i]+res[i+1]                         # res.append(a3)
       res.append(a3)
    print(res)


    res=[1,1]
    while len(res)<long:
        a3=res[-1]+res[-2]

