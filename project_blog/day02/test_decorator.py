import time

# 原有函数
# def func():
#     print('hello')
#     time.sleep(1)
#     print('world')

# 1.扩展函数功能,计算函数执行的时间消耗
def func_ex():
    startTime=time.time()
    print('hello')
    time.sleep(1)
    print('world')
    endTime=time.time()
    timeout=endTime-startTime
    print('timeout is %s'%timeout)

# 2.扩展函数功能[不修改原有函数],将被扩展的函数名作为新函数的参数
def deco(func):
    startTime=time.time()
    func()
    endTime = time.time()
    timeout = endTime - startTime
    print('timeout is %s' % timeout)

# 3.使用装饰器[不修改原有函数],将被扩展的函数名作为新函数的参数
# 与2的区别是,返回内部函数[函数编写嵌套,闭包]
# 实质:装饰器也是一个函数
# 参数:装饰器的参数是被修饰(被扩展功能)的函数
# 返回值:返回内部函数[内部函数的作用是扩展原有函数的功能]
def deco2(func):
    def wrapper():
        startTime = time.time()
        func()
        endTime = time.time()
        timeout = endTime - startTime
        print('timeout is %s' % timeout)
    # 返回内部函数,并没有调用
    return wrapper

@deco2
def func2():
    print('hello')
    time.sleep(1)
    print('world')


# 使用装饰器修饰带参数的函数
def deco3(func):
    def wrapper(a,b):
        startTime = time.time()
        func(a,b)
        endTime = time.time()
        timeout = endTime - startTime
        print('timeout is %s' % timeout)
    return wrapper

# 原始函数
@deco3
def func_param(a,b):
    print('函数的功能是求两个数值的和')
    time.sleep(1)
    print('result is %s'%(a+b))

# 使用装饰器修饰带参数的函数,被修饰的参数个数不定
def deco4(func):
    def wrapper(*args,**kwargs):
        startTime = time.time()
        func(*args,**kwargs)
        endTime = time.time()
        timeout = endTime - startTime
        print('timeout is %s' % timeout)
    return wrapper
@deco4
def sum_two(a,b):
    print('两个数值的和:')
    time.sleep(1)
    print('a+b=%s'%(a+b))
@deco4
def sum_three(a,b,c):
    print('三个数值的和:')
    time.sleep(1)
    print('a+b+c=%s' % (a + b+c))


# 带参数的装饰器[装饰器带参数,需要定义三层装饰器]
def deco_param(expire):
    def _deco_param(func):
        def wrapper():
            startTime = time.time()
            print('expire is %s'%expire)
            func()
            endTime = time.time()
            timeout = endTime - startTime
            print('timeout is %s' % timeout)
        return wrapper
    return _deco_param


# 原有函数
@deco_param(10)
def func3():
    print('hello')
    time.sleep(1)
    print('world')


if __name__ == '__main__':
    # func()
    # func_ex()
    # deco(func)
    # func2是有装饰器的,调用func2,相当于调用deco2(func2)
    # 由于deco2 返回 wrapper函数,所以,相当于调用了内部函数wrapper
    # 而wrapper就包含了对原函数的扩展
    # func2()
    # func_param(10,20)
    # sum_two(20,30)
    # sum_three(20,30,40)
    func3()