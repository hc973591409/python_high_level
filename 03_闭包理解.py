def test(num):
    print("%d ----test----" % num)

    def test_in(num_in):
        print("-----内函数返回-----")
        res = num + num_in
        return res
    print("-----外函数 返回-----")
    return test_in


# 限定一个ret <===>  ret = test_in(x(占位))
# 此处的20是给到外函数
ret = test(20)

# 通过上面定义的函数访问内部函数,此处的100给到内函数
print(ret(100))

print(ret(200))


def counter(start=0):
    count = [start]

    def incr():
        count[0] += 1
        return count[0]

    return incr


c = counter(5)
print(c())
print(c())
print(c())
print(c())

# 利用闭包实现对一次函数的求解,
# 分析 y=a*x+b  给出(a,b),可以得到一条曲线, 当给出x的值就可以得到y


def fun(a, b):
    def fun_in(x):
        return a*x + b
    return fun_in


fun1 = fun(1, 2)
fun2 = fun(0.5, 4)
fun3 = fun(-1, 2)

print(fun1(2))
print(fun2(2))
print(fun3(2))
