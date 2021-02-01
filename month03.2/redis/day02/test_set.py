import redis

r=redis.Redis(password='123456')

r.sadd('武将', '张飞', '赵云', '马超', '周瑜')
r.sadd('文臣','周瑜','诸葛亮','司马懿','郭嘉')
res1=r.sdiff('武将', '文臣')
res2=r.sdiff('文臣', '武将')
res3=r.sinter('武将', '文臣')
res4=r.sunion('武将', '文臣')
lst_all=[]
for r in res3:
    lst_all.append(r.decode())
print(lst_all)


