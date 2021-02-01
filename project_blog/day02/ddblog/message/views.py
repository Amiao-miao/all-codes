import json

from django.contrib.sites import requests
from django.http import JsonResponse
from django.shortcuts import render
from tools.login_dec import login_check
from topic.models import Topic
from .models import Message
# Create your views here.
# 功能是用来发表评论的,需要做登录认证

@login_check
def message_view(request,topic_id):
    # 1 限定前端发送的是POST请求
    if request.method!='POST':
        result={'code':10400,'error':'请发送post请求'}
        return JsonResponse(result)
    # 2 从客户端获取评论内容,parent_id[0]
    json_str=request.body
    json_obj=json.loads(json_str)
    content=json_obj['content']
    parent_id=json_obj.get('parent_id',0)
    # 3 验证topic_id对应的对应的文章是否存在,获取topic对象
    try:
        topic=Topic.objects.get(id=topic_id)
    except:
        result = {'code': 10401, 'error': '文章id有误!'}
        return JsonResponse(result)
    # 4 从请求对象中获取用户对象
    user=request.myuser
    # 5 数据入库
    Message.objects.create(topic=topic,content=content,
                           user_profile=user,
                           parent_message=parent_id)
    # 6 返回
    return JsonResponse({'code':200})