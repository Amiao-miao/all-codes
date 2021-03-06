
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

html="""
# <form method='get' action="/test_get">
#     <p>
#     姓名:<input type="text" name="uname">
#     </p>
#     <p>
#     <input type="submit" value="提交">
#     </p>
# </form>
# 
# """

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showData(self):
        return '姓名:%s,年龄:%s'%(self.name,self.age)


def test_get(request):
    # 后端收到客户端提交的查询字符串,打印
    # 1.要求查询字符串中必须存在名称为uname的数据
    # uname=request.GET['uname']
    # 2.换一种方式获取,试着获取,没有也不报错,值为None而已
    # uname=request.GET.get('uname')
    # 3.试着获取,有值拿值,没有值,使用默认值,第二个参数为默认值
    uname = request.GET.get('uname','tedu')
    print(uname)
    # 4.如果同一个名称有多个值,使用getlist可以获取一个列表
    print(request.GET.getlist('a')[0])
    return HttpResponse(html)

html2="""
<form method='post' action="/test_post">
    <p>
    姓名:<input type="text" name="uname">
    </p>
    <p>
    <input type="submit" value="提交">
    </p>
</form>

"""
def test_post(request):
    if request.method=='GET':
        return HttpResponse(html2)
    elif request.method=='POST':
        uname=request.POST['uname']
        # 与GET类似,也有
        # request.POST.get('unmae',默认值)
        # request.POST.getlist(表单元素的名称)
        return HttpResponse(f'北京欢饮您,{uname}')

def birthday(request):
    year=request.GET.get('year')
    month=request.GET.get('month')
    day=request.GET.get('day')
    return HttpResponse(f'您的生日:{year}年{month}月{day}日')

def Hello():
    return '北京欢迎你'

def test_html(request):
    # 返回一个模板页
    # 方式一
    # t=loader.get_template('test_html.html')
    # html=t.render()
    # return  HttpResponse(html)

    # 方式二
    # dict1={}
    # dict1['name']='aid2010'
    # dict1['count']=500
    # dict1['citys'] = ['北京','上海','杭州','武汉']
    # dict1['distr']={'北京':1500,'上海':150,'杭州':400,'武汉':900}
    # dict1['p1']=Person('佟大为',40)
    # dict1['function1'] = Hello
    # dict1['script']='<script>alert("Hello World")</script>'
    # return render(request,'test_html.html',dict1)

    # 方式三[推荐的方式]
    name='aid2010,we are family'
    count=500
    citys = ['北京', '上海', '杭州', '武汉']
    distr={'北京': 1500, '上海': 150, '杭州': 400, '武汉': 900}
    p1=Person('佟大为', 40)
    function1 = Hello
    script='<script>alert("Hello World")</script>'

    persons=['关羽','黄忠','张飞','赵云','马超']
    # persons=[]
    return render(request,'test_html.html',locals())

def test_calc(request):
    if request.method=="GET":
        return render(request,'test_calc.html')
    elif request.method=="POST":
        x=request.POST['x']
        y=request.POST['y']
        # 为空判断
        if not x or not y:
            return HttpResponse('请输入数据')
        # 数值判断
        try:
            x=int(x)
            y=int(y)
        except:
            return HttpResponse('请输入一个整数值')
        result=0
        op=request.POST['op']
        if op=="add":
            result=x+y
        elif op=="sub":
            result=x-y
        elif op=="mul":
            result=x*y
        elif op=="div":
            result=x/y
        return render(request,'test_calc.html',locals())