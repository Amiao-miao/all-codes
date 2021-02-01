from ddblog.celery import app
from tools.sms import YuoknTongXin

@app.task
def send_sms(phone,code):
    aid = '8aaf0708773733a80177433d7c750705'
    atoken = 'e0718509c4f942a29bfb9be971afedea'
    appid = '8aaf0708773733a80177433d7d3f070b'
    tid = '1'

    # 1 创建云通信对象
    x = YuoknTongXin(aid, atoken, appid, tid)
    # 2 发送短信
    res = x.run(phone, code)
    # 3 返回信息
    print(res)