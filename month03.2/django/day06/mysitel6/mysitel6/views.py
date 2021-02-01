from django.http import HttpResponse


def set_cookies(request):
    resp=HttpResponse('设置cookies成功!')
    resp.set_cookie('uname','aid2010',60)
    return resp

def get_cookies(request):
    uname=request.COOKIES.get('uname','default value')
    result='uname is %s'%uname
    return HttpResponse(result)

def del_cookies(request):
    resp = HttpResponse('删除cookies成功!')
    resp.delete_cookie('uname')
    return resp

def set_session(request):
    request.session['uname']='tedu'
    return HttpResponse('set session is ok')

def get_session(request):
    uname=request.session.get('uname','default value')
    result='uname is %s'%uname
    return HttpResponse(result)

def del_session(request):
    if 'uname' in request.session:
        del request.session['uname']
    return HttpResponse('delete session is ok')