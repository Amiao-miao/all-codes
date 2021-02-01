from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import UserProfile
import hashlib
import jwt
import time
from django.conf import settings
from tools.login_dec import login_check
import random
from django.core.cache import cache
from tools.sms import YuoknTongXin
from .tasks import send_sms
class UserView(View):
    # 处理 v1/users/<username> 的GET请求
    def get(self,ruquest,username=None):
        if username:
            #返回指定用户的信息
            try:
                user=UserProfile.objects.get(username=username)
            except:
                result={'code':10104,'error':'用户名称有误!'}
                return JsonResponse(result)

            if ruquest.GET.keys():
                #获取指定信息
                data={}
                for k in ruquest.GET.keys():
                    if k=='password':
                        continue
                    if hasattr(user,k):
                        data[k]=getattr(user,k)
                result={'code':200,'username':username,
                            'data':data}
            else:
                #返回指定用户的全量信息
                result={'code':200,'username':username,
                        'data':{'info':user.info,'sign':user.sign,
                                'nickname':user.nickname,
                                'avatar':str(user.avatar)
                                }}
            return JsonResponse(result)
        else:
            return HttpResponse('-user get-')

    # 处理v1/users的POST 请求
    def post(self,request):
        # 1.获取前端给后端的json串
        json_str=request.body
        # 2.把json串反序列化为对象
        json_obj=json.loads(json_str)
        # 3.从对象[字典]中获取数据
        username= json_obj['username']
        email = json_obj['email']
        phone= json_obj['phone']
        password_1 = json_obj['password_1']
        password_2 = json_obj['password_2']
        # 获取从前端拿到的验证码(字符串类型)
        sms_num = json_obj['sms_num']
        # 从缓存中获取已经保存的验证码
        cache_key = 'sms_%s' % phone
        code=cache.get(cache_key)
        # 校对验证码
        if not code:
            result={'code':10110,'error':'从缓存中获取验证码失败'}
            return JsonResponse(result)
        if int(sms_num)!=code:
            result = {'code': 10111, 'error':'输入验证码错误'}
            return JsonResponse(result)

        # 4.数据检查
        # 4.1 检查注册的用户是否可以注册
        old_user=UserProfile.objects.filter(username=username)
        if old_user:
            result={'code':10100,'error':'用户名已注册'}
            return JsonResponse(result)
        # 4.2 两次密码是否一致
        if password_1!=password_2:
            result = {'code': 10101, 'error': '两次密码不一致'}
            return JsonResponse(result)
        # 4.3 添加密码的hash值
        md5=hashlib.md5()
        md5.update(password_1.encode())
        password_h=md5.hexdigest()

        # 5. 插入数据[仍然需要try]
        try:
            user=UserProfile.objects.create(username=username,
                                            password=password_h,
                                            email=email,
                                            phone=phone,
                                            nickname=username)
        except:
            result = {'code': 10102, 'error': '用户名已注册'}
            return JsonResponse(result)

        # 6.如何记住登录状态
        # 以前的云笔记项目中,我们使用的session(只能用于浏览器)保存登录状态
        # 博客项目中使用刚刚学习的token
        token=make_token(username)
        #print(token)
        #为什么要decode?
        # 将生成的字节串转换为字符串
        token=token.decode()
        #print(token)
        return JsonResponse({'code':200,'username':username,
                             'data':{'token':token}})

    # 处理 /v1/users/<username>的put请求
    @method_decorator(login_check)
    def put(self,request,username):
        # 1 获取前端传递的json串
        json_str=request.body
        # 2 将json串反序列化为对象
        json_obj=json.loads(json_str)
        # 3 获取要修改的用户
        user=request.myuser  # 记录着登录用户的对象
        # 4 修改
        user.sign=json_obj['sign']
        user.nickname = json_obj['nickname']
        user.info = json_obj['info']
        # 5 保存
        user.save()
        # 6 返回
        result={'code':200,'username':user.username}
        return JsonResponse(result)


def make_token(username,expire=3600*24):
    key=settings.JWT_TOKEN_KEY
    now=time.time()
    payload={'username':username,'exp':now+expire}
    # 生成token
    return jwt.encode(payload,key,algorithm='HS256')


@login_check
def user_avatar(request,username):
    if request.method!='POST':
        result={'code':10105,'error':'只接收post请求'}
        return JsonResponse(result)
    # 从request获取已经登录的用户
    user=request.myuser
    # 修改用户的头像
    user.avatar=request.FILES['avatar']
    # 保存
    user.save()
    # 返回
    result={'code':200,'username':user.username}
    return JsonResponse(result)

def sms_view(request):
    # 1 获取前端提交的数据
    json_str=request.body
    # 2 json串反序列化为对象
    json_obj=json.loads(json_str)
    # 3 获取手机号
    phone=json_obj['phone']
    # 4 生成随机的验证码
    code=random.randint(1000,9999)
    # 5 将验证码存储到缓存(redis)中
    cache_key='sms_%s'%phone
    cache.set(cache_key,code,180)
    print(phone,code)
    # 6 向指定的手机号发送短信验证请求[将以下的数据写到配置文件中]
    aid = '8aaf0708773733a80177433d7c750705'
    atoken = 'e0718509c4f942a29bfb9be971afedea'
    appid = '8aaf0708773733a80177433d7d3f070b'
    tid = '1'

    #同步方式
    # # 1 创建云通信对象
    # x = YuoknTongXin(aid, atoken, appid, tid)
    # # 2 发送短信
    # res = x.run(phone, code)
    # # 3 打印返回信息
    # print(res)


    #异步方式
    send_sms.delay(phone,code)
    return JsonResponse({'code':200})
