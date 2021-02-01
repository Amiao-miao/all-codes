from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User
import hashlib
# Create your views here.
def login_view(request):
    if request.method=='GET':
        if 'uname' in request.session and 'uid' in request.session:
            return HttpResponse('您已登录')
        return render(request,'user/login.html')
    elif request.method=='POST':
        # 1.获取数据
        username=request.POST['username']
        password=request.POST['password']
        # 2.表单检查
        if not username or not password:
            return HttpResponse('用户名或密码不能为空!')
        # 3.查看有无名称为username的用户
        try:
            user=User.objects.get(username=username)
        except:
            return HttpResponse('用户名或密码错误!')
        # 4.检查密码是否正确
        md5=hashlib.md5()
        md5.update(password.encode())
        password_h=md5.hexdigest()
        if password_h !=user.password:
            return HttpResponse('用户名或密码错误!')
        # 使用session保存登录的状态
        request.session['uname']=username
        request.session['uid']=user.id

        return HttpResponseRedirect('/user/login')

def reg_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        #1.从表单元素中获取数据
        username=request.POST['username']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
        # print(username,password_1,password_2)
        # 2.数据检查
        # 2.1 为空检查
        if not username or not password_1:
            return HttpResponse('用户名或密码不能为空!')
        # 2.2 两次密码要一致
        if password_1 != password_2:
            return HttpResponse('两次密码要一致!')
        # 2.3 用户名称不能重复
        old_user=User.objects.filter(username=username)
        if old_user:
            return HttpResponse('用户名已占用!')
        # 3.计算口令(密码)的Hash值
        md5=hashlib.md5()
        md5.update(password_1.encode())
        password_h=md5.hexdigest()
        # 4.数据入库
        try:
            User.objects.create(username=username,
                                password=password_h)
        except:
            return HttpResponse('用户名被占用!')
        return HttpResponse('注册成功')

def logout_view(request):
    if 'uname' in request.session:
        del request.session['uname']
    if 'uid' in request.session:
        del request.session['uid']
    return HttpResponse('用户退出成功')