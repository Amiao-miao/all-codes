from django.http import JsonResponse
import jwt
from django.conf import settings
from user.models import UserProfile

def login_check(func):
    def wrap(request,*args,**kwargs):
        # 在请求对象中获取前端提交过来的token
        token=request.META.get('HTTP_AUTHORIZATION')
        if not token:
            result={'code':403,'error':'请登录!'}
            return JsonResponse(result)
        # token的校验
        try:
            # decode方法中,首先会验签,签名是否有效;
            # 验签通过后,从payload获取有效期,判断token是否在有效期内
            payload=jwt.decode(token,settings.JWT_TOKEN_KEY,algorithm='HS256')
        except:
            result={'code':403,'error':'please login !'}
            return JsonResponse(result)
        # 从结果中获取私有声明
        username=payload['username']
        # 根据用户名称获取用户对象
        user=UserProfile.objects.get(username=username)
        # 将用户对象作为request的附加属性
        request.myuser=user
        # 调用所修饰的函数
        return func(request,*args,**kwargs)

    return wrap


# 获取文章的访问者的信息
def get_user_by_request(request):
    # 没有登录的用户[游客]
    token=request.META.get('HTTP_AUTHORIZATION')
    if not token:
        return None
    try:
        payload=jwt.decode(token,settings.JWT_TOKEN_KEY)
    except:
        return None
    username=payload['username']
    return username
