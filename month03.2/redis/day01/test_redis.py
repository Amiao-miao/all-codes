import redis

# 创建redis数据库的连接对象
r=redis.Redis(host='127.0.0.1',port=6379,db=0,
              password='123456')

# 1.通用命令对应的Python方法
# byte 字节,返回的值的类型都是字节串
print(r.keys('*'))
# 判断键是否存在
print(r.exists('lk1'),r.exists('lk2'))

# 2.字符串类型的操作
r.set('name','aid2010班',1000)
print(r.get('name').decode())
# 设置多个字符串的值,参数使用字典
print(r.mset({'a': 100, 'b': 200, 'c': 300}))
# 获取多个,参数用列表
print(r.mget(['a', 'b', 'c']))

# 3.列表类型的操作
r.

