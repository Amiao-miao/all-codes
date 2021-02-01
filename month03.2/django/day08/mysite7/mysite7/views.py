import os
import time

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
import csv

from django.views.decorators.csrf import csrf_exempt
# 在视图函数中如果使用当前的配置文件时,
# Django要求我们导入的是它内置的settings,而不是我们这个
from django.conf import settings
from test_upload.models import Content
from django.http import Http404
@cache_page(30)
def test_cache(request):
    t1=time.time()
    print('--------------views in---------------')
    # 模拟耗时操作

    time.sleep(3)
    return HttpResponse('time is %s'%t1)


def test_csrf(request):
    if request.method=='GET':
        return render(request,'test_csrf.html')
    elif request.method=='POST':
        username=request.POST['username']
        return HttpResponse('username is %s'%username)

def test_page(request):
    # 1.要分页的数据
    list1=['a','b','c','d','e']
    # 2.创建Paginator对象
    paginator=Paginator(list1,2)
    # 3.从查询字符串获取当前页的页码
    cur_page=request.GET.get('page',1)
    # 4.创建page对象
    page=paginator.page(cur_page)
    # 5.返回页面
    return render(request,'test_page.html',locals())

def test_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mybook.csv"'
    # 创建一个csv的写入器
    writer=csv.writer(response)
    # 写入标题
    writer.writerow(['图书编号','图书名称'])
    # 准备数据
    all_books=[
        {'id':1,'title':'Python'},
        {'id':2, 'title': 'C++'},
        {'id':3, 'title': 'Java'},
    ]
    # 写入数据
    for book in all_books:
        writer.writerow([book['id'],book['title']])
    return response

@csrf_exempt
def test_upload(request):
    if request.method=='GET':
        return render(request,'test_upload.html')
    elif request.method=='POST':
        # 获取文件对象
        afile=request.FILES['myfile']
        # 获取表单元素的值
        title=request.POST['title']

        # 第一种文件上传方式
        # 生成一个服务器端文件的全路径
        # GUID(全局唯一标识符) 防止重名
        # filename=os.path.join(settings.MEDIA_ROOT,afile.name)
        # with open(filename,'wb+') as f:
        #     # 读取文件内容
        #     data=afile.file.read()
        #     f.write(data)
        # result='文件%s上传成功!文件描述%s'%(afile.name,title)
        # return HttpResponse(result)

        # 第二种文件上传方式
        Content.objects.create(title=title,myfile=afile)
        return HttpResponse('文件%s上传成功!文件描述%s'%(afile.name,title))

def xxx_view( ):
    raise Http404
