import redis

r=redis.Redis(password='123456')
# 任务信息:任务类别_发送者_接受者_内容
task='%s_%s_%s_%s'%('sendMail','123@qq.com','456@qq.com','hello world')
# 添加任务
r.lpush('pylk1',task)