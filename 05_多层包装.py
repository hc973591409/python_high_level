def makeBlod(fun):
    def inner():
        return '<B>'+fun()+'</B>'
    return inner


def makeItcast(fun):
    def inner():
        return '<I>'+fun()+'</I>'
    return inner


@makeBlod            # 多层包装,先包装,后执行 需要等待下层包装完成返回函数才能接着包装
@makeItcast
def func():
    return "hello world"


print(func())


import time


def funct(func):
    def inner():
        print("%s %s" % (func.__name__, time.ctime()))
        func()

    return inner

@funct
def foo():
    print('I ame foo')

foo()