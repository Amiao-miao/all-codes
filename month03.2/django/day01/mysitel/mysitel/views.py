from django.http import HttpResponse

# 视图函数
# 参数为请求对象
# 返回值为响应对象
def page_2003(request):
    return HttpResponse('这是编号为2003的页面')

def page_2004(request):
    return HttpResponse('这是编号为2004的页面')

def page_index(request):
    return HttpResponse('<h1>不要找小火箭页面啦,我是默认首页</h1>')

def page_num(request,num):
    return HttpResponse(f'path转换器:这是编号为{num}的页面')

def page_data(request,data):
    return HttpResponse(f'data:{data}')

def page_path(request,data2):
    return HttpResponse(f'path:{data2}')

def mymath(request,n1,giao,n2):
    if giao not in ['add','sub','mul']:
        return HttpResponse('运算有误')
    result=0
    if giao=='add':
        result=n1+n2
    elif giao=='sub':
        result=n1-n2
    elif giao=='mul':
        result=n1*n2
    # 测试request对象的使用,从request对象中获取客户端请求的信息
    print(request.method)
    print(request.path_info)
    return HttpResponse(f'计算结果为{result}')




def birthday_view(request,y,m,d):
    return HttpResponse(f'您的生日为:{y}年{m}月{d}日')