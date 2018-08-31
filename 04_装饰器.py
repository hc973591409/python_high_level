def w(func):
    def inner():
        print("----验证1----")
        print("----验证2----")
        print("----验证3----")
        func()
    return inner


@w          # <==> f1 = w(f1)
def f1():
    print("-------f1--------")


@w
def f2():
    print("-------f2--------")


@w
def f3():
    print("-------f3--------")


@w
def f4():
    print("-------f4--------")


f1()
f2()
f3()
f4()
