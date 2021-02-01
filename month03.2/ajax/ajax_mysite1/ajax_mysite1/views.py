from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def test_xhr(request):
    return render(request,'test_xhr.html')

def test_xhr_get(request):
    return render(request, 'test_xhr_get.html')

def test_xhr_get_server(request):
    return HttpResponse('This is Ajax Data!')

def test_jq_get(request):
    return render(request,'test_jq_get.html')

def test_json(request):
    return render(request,'test_json.html')

def make_json_server(request):
    # 1.字典
    # dict1={'name':'tedu','age':18}
    # return JsonResponse(dict1)
    # 2.列表或元组
    list1=[
        {'name':'tedu','age':18},
        {'name': 'tedu2', 'age': 28}
    ]
    return JsonResponse(list1,safe=False)

def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    elif request.method=='POST':
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        print(uname,pwd)
        return HttpResponse('%s注册成功'%uname)