import redis

r=redis.Redis(password='123456')


if __name__ == '__main__':
    print(r.keys("*"))
    r.flushdb()
    #操作列表
    r.rpush('spider:urls','01_baidu.com',
            '02_taobao.com','03_sina.com',
            '04_jd.com','05_xxx.com')
    #查看列表中所有元素
    r.lrange('spider:urls',0,-1)
    # 查看列表长度
    print(r.llen('spider:urls'))
    # 修改
    r.lset('spider:urls',0,'01_tmall.com')
    # 弹出最后一个元素
    print(r.rpop('spider:urls'))
    # 删除
    r.lrem('spider:urls', 0, '02_taobao.com')
    # 剔除列表中的其他元素，只剩前3条(截取)
    r.ltrim('spider:urls',0,2)