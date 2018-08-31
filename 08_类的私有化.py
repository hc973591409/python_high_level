# xx: 公有变量
# _x: 单前置下划线,私有化属性或方法，from somemodule import *禁止导入,类对象和子类可以访问
# __xx：双前置下划线,避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)
# __xx__:双前后下划线,用户字空间的魔法对象或属性。例如:__init__ , __ 不要自己发明这样的名字
# xx_:单后置下划线,用于避免与Python关键词的冲突名
# 子类不能继承私有方法和私有属性
class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")
    # 由于我们调用设置私有属性比较麻烦，所以有了下面这句话
    money = property(getMoney, setMoney)

a = Money()
print(a.money) # 会自动调用读取方法
print(type(100))
a.money=100         # 调用写方法会自动调用设置方法
print(a.money)

# 第二种写，就不用多想两个函数名，想想都开心

class Money1(object):
    def __init__(self):
        self.__money = 0

    # 定义为属性函数
    @property
    def money(self):
        return self.__money

    # 属性函数的设置方法
    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")

b = Money1()
print(b.money) # 会自动调用读取方法
print(type(100))
b.money=100         # 调用写方法会自动调用设置方法
print(b.money)