# 垃圾回收
#   1. 小整数对象池
# 整数在程序中的使用非常广泛，Python为了优化速度，使用了小整数对象池， 避免为整数频繁申请和销毁内存空间。
# Python 对小整数的定义是 [-5, 257) 这些整数对象是提前建立好的，不会被垃圾回收。在一个 Python 的程序中，所有位于这个范围内的整数使用的都是同一个对象.
# 同理，单个字母也是这样的。
# 但是当定义2个相同的字符串时，引用计数为0，触发垃圾回收

# 2. 大整数对象池
# 每一个大整数，均创建一个新的对象。

# 3. intern机制
a1 = "HelloWorld"
a2 = "HelloWorld"
a3 = "HelloWorld"
a4 = "HelloWorld"
a5 = "HelloWorld"
a6 = "HelloWorld"
a7 = "HelloWorld"
a8 = "HelloWorld"
a9 = "HelloWorld"
# 所以python中有这样一个机制——intern机制，让他只占用一个”HelloWorld”所占的内存空间。
# 靠引用计数去维护何时释放。
print(a1 is a9)

# 小整数[-5,257)共用对象，常驻内存
# 单个字符共用对象，常驻内存
# 单个单词，不可修改，默认开启intern机制，共用对象，引用计数为0，则销毁

# python2
# 字符串（含有空格），不可修改，没开启intern机制，不共用对象，引用计数为0，销毁
# 这个不适用于python3 python3还是引用计数

b1 = "Hello  World"
b2 = "Hello  World"
b3 = "Hello  World"
b4 = "Hello  World"
b5 = "Hello  World"
b6 = "Hello  World"
b7 = "Hello  World"
b8 = "Hello  World"
b9 = "Hello  World"

print(b1 is b9)


# 1. Garbage collection(GC垃圾回收)
# python的每个东西都是对象，本质为C中的结构体，一个对象+ 引用计数
# typedef struct_object {
#     int ob_refcnt;
#     struct_typeobject *ob_type;
# } PyObject;
# PyObject是每个对象必有的内容，其中ob_refcnt就是做为引用计数。当一个对象有新的引用时，
# 它的ob_refcnt就会增加，当引用它的对象被删除，它的ob_refcnt就会减少
# 引用计数机制的优点：

# 简单
# 实时性：一旦没有引用，内存就直接释放了。不用像其他机制等到特定时机。
# 实时性还带来一个好处：处理回收内存的时间分摊到了平时。

# 引用计数机制的缺点：

# 维护引用计数消耗资源
# 循环引用
# list1 = []
# list2 = []
# list1.append(list2)
# list2.append(list1)

# list1与list2相互引用，如果不存在其他对象对它们的引用，list1与list2的引用计数也
# 仍然为1，所占用的内存永远无法被回收，这将是致命的。 对于如今的强大硬件，缺点1尚
# 可接受，但是循环引用导致内存泄露，注定python还将引入新的回收机制。(标记清除和分
# 代收集)

# 2.1 应用程序那颗跃动的心
# GC系统所承担的工作远比"垃圾回收"多得多。实际上，它们负责三个重要任务。它们

# 为新生成的对象分配内存
# 识别那些垃圾对象，并且
# 从垃圾对象那回收内存。
