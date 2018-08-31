# 在小整数,1占用一个空间
a = 1
b = 1
print(a is b)
# True
# 浅拷贝
c = [11, 22, 33]
d = c
print(d is c)
# True
e = {"name": "xiaoming"}
f = e
e["age"] = 19
print(f)
# {'name': 'xiaoming', 'age': 19}
# 一般的赋值号都是浅拷贝

import copy
g = [33, 44, 55]
# deepcopy(g)是用递归的方式拷贝，内部有引用其他变量，统统重新拷贝一份
# copy函数只是拷贝表面一层，如果内部有引用其他变量，不重新拷贝，重要数据慎用，不重要的可以节约内存

h = copy.deepcopy(g)
print(g is h)
# False
