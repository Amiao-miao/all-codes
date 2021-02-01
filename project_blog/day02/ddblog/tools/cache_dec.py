from .login_dec import get_user_by_request
from django.core.cache import cache

def topic_cache(expire):
    def _topic_cache(func):
        def wrapper(request,*args,**kwargs):
            # 如果是文章的详情页,直接调用
            if 't_id' in request.GET.keys():
                return func(request,*args,**kwargs)
            # 是否是博主访问自己
            # 访问者名称
            visitor_name=get_user_by_request(request)
            # 作者名称
            author_name=kwargs['author_id']
            if visitor_name==author_name:
                # 博主访问自己
                # get_full_path() 返回带查询字符串的path
                # get_full_path()有几种情况:
                # 1.v1/tedu/topics
                # 2.v1/tedu/topics?category=tec
                # 3.v1/tedu/topics?category=no-tec
                cache_key='topic_cache_self_%s'%(request.get_full_path())
            else:
                # 非博主访问
                # get_full_path()有几种情况:
                # 1.v1/tedu/topics
                # 2.v1/tedu/topics?category=tec
                # 3.v1/tedu/topics?category=no-tec
                cache_key = 'topic_cache_%s' % (request.get_full_path())
            print('--------cache key is %s--------'%cache_key)
            # 缓存思想:有缓存,访问缓存;没有缓存,调用视图函数,并写入缓冲返回
            res=cache.get(cache_key)
            if res:
                print('------cache in---------')
                return res
            res=func(request,*args,**kwargs)
            cache.set(cache_key,res,expire)
            return res
        return wrapper
    return _topic_cache