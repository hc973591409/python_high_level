def list_make():
    # range(start, stop[, step]) -> list of integers
    test_list = [x for x in range(1, 10) if x % 2 == 0]
    test_list = [x for x in range(1, 10, 3)]
    test_list = range(5)          # 不迭代返回的就是迭代器
    for x in test_list:
        print(x)

    # start:计数从start开始。默认是从0开始。例如range（5）等价于range（0， 5）;
    # stop:到stop结束，但不包括stop.例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
    # step:每次跳跃的间距，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)


def make_map():
    # map函数

    # map函数会根据提供的函数对指定序列做映射
    # 函数只需要一个参数的
    my_list = map(lambda x: x*x, [1, 2, 3, 4])
    print(type(my_list))         # <class 'map'>
    for x in my_list:
        print(x)

    # 函数需要两个参数的
    my_list = map(lambda x, y: x+y, [1, 2, 3, 4], [5, 6, 7, 8, 9])

    print(type(my_list))         # <class 'map'>
    for x in my_list:
        print(x)

    # 也可以传递一个实际的函数
    def f(x, y):
        return x, y

    my_list = map(f, [1, 2, 3, 4], ['A', 'B', 'C', 'D'])
    print(type(my_list))         # <class 'map'>
    for x in my_list:
        print(x)


def filter_make():
    # filter函数会对指定序列执行过滤操作
    # filter(function or None, sequence) -> list, tuple, or string
    # function:接受一个参数，返回布尔值True或False
    # sequence:序列可以是str，tuple，list

    my_list = filter(lambda x: x % 2 == 0, [x for x in range(1, 11)])
    print(type(my_list))         # <class 'filter'>
    for x in my_list:
        print(x)


def func_make():
    from functools import reduce
    # 需要注意的是python已经移除函数，需要导入才能使用，python2可以直接使用
    # reduce函数，reduce函数会对参数序列中元素进行累积
    # reduce(function, sequence[, initial]) -> value
    # function:该函数有两个参数
    # sequence:序列可以是str，tuple，list
    # initial:固定初始值
    value = reduce(lambda x, y: x+y, [1, 2, 3, 4])
    print(value)

    value = reduce(lambda x, y: x+y, [1, 2, 3, 4], 5)
    # 相当于初始值value = 5 然后+[1,2,3,4]
    print(value)


def set_make():
    # 集合set集合与之前列表、元组类似，可以存储多个数据，但是这些数据是不重复的
    # 集合对象还支持union(联合), intersection(交), difference(差)和
    # sysmmetric_difference(对称差集)等数学运算.
    x = set('abcd')
    print(x)
    y = set(['h', 'e', 'l', 'l', 'o', 'a'])
    print(y)
    z = set('spam')
    print(z)
    # 交集
    print(y & z)
    print(x & z)
    # 并集
    print(x | z)
    # x-y #差集
    print(x-y)
    # x^z #对称差集(在x或z中，但不会同时出现在二者中)
    print(x ^ z)

    print(len(x))

    print(len(y))

    print(len(z))


import functools
# 偏函数
# 把一个函数的某些参数设置默认值，返回一个新的函数，调用这个新函数会更简单。

def partial_make():
    def showarg(*args, **kw):
        print(args)
        print(kw)


    # 设置1，2，3为默认参数
    p1 = functools.partial(showarg, 1, 2, 3)
    p1()
    p1(4, 5, 6)
    p1(name='huchao', age=22)

    p2 = functools.partial(showarg,a=3,b='linux')
    p2()
    p2(1,2,3)
    # 覆盖了默认参数
    p2(a=4,b='ubuntu')

# wraps函数
# 使用装饰器时，有一些细节需要被注意。例如，被装饰后的函数其实已经是另外一个函数了（函数名等函
# 数属性会发生改变）。
# 添加后由于函数名和函数的doc发生了改变
def test():
    def note(func):
        "note function"
        def wrapper():
            "wrapper function"
            print('note something')
            return func()
        return wrapper

    @note
    def test():
        "test function"
        print('I am test')

def note(func):
    "note function"
    @functools.wraps(func)
    def wrapper():
        "wrapper function"
        print('note something')
        return func()
    return wrapper

@note
def test():
    "test function"
    print('I am test')

test()
print(test.__doc__)