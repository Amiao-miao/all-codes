import time

from django.http import HttpResponse
from django.views.decorators.cache import cache_page


@cache_page(30)
def test_cache(request):
    t1=time.time()
    print('--------------views in---------------')
    # 模拟耗时操作

    time.sleep(3)
    return HttpResponse('time is %s'%t1)


def test_mw(request):
    print('my view in')
    return HttpResponse('my middleware view!')