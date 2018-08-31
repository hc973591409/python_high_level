# 在Python中，这种⼀边循环⼀边计算 的机制，称为⽣成器：generator
# 。第⼀种⽅法很简单，只要把⼀个列表⽣ 成式的	[	]	改成	(	)
L = [x*2 for x in range(5)]
print(type(L))
# <class 'list'>

G = (x*2 for x in range(5))
print(type(G))
# <class 'generator'>
# print(next(G))
# print(next(G))
# print(next(G))
# 超过生成器的个数，就会抛出异常
# 循环遍历G
# ⽣成器保存的是算法，每次调⽤	next(G)	，就计算出	G	的下⼀个元素的值， 直到计算到最后⼀个元素，没有更多的元素时，
# 抛出	StopIteration	的异常。 当然，
# 这种不断调⽤	next()	实在是太变态了，正确的⽅法是使⽤	for	循环， 因为⽣成器也是可迭代对象。
for x in G:
    print(x)

# 	创建⽣成器⽅法2


def fib(times):
    n = 0
    a, b = 0, 1
    while n < times:
        a, b = b, a+b
        print(b, end=',')
        n += 1


def fibn(times):
    n = 0
    a, b = 0, 1
    while n < times:
        a, b = b, a+b
        # 相当于返回b，但是函数每次执行到这个都会暂定，直到下一次进来取值
        yield b
        n += 1


x = fibn(10)

while True:
    try:
        a = next(x)   # fibn(10) 是一个列表生成器 ，一般我们不这么访问
        print(a)
    except:
        print("列表生成器结束")
        break
