import redis

r=redis.Redis(password='123456')

# 1.测试前.清一下库
r.flushdb()
# 2.操作hash
r.hset('pyhk1','name','aid2010')
print(r.hget('pyhk1', 'name'))
r.hmset('pyhk1',{'age':18,'city':'北京'})
# 结果是字典
all=r.hgetall('pyhk1')
for i in all:
    print(i.decode())

# 结果是列表
print(r.hvals('pyhk1'))
# 结果是列表
print(r.hkeys('pyhk1'))