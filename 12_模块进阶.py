# 哈希加密算法
import hashlib
def hash_test():
    m = hashlib.md5()
    # <sha256 HASH object @ 0x006DC788>
    print(m)
    #更新哈希对象以字符串参数
    str1 = 'huchao'.encode('utf-8')
    m.update(str1)
    #返回十六进制数字字符串
    print(m.hexdigest())

# hash应用
import datetime

KEY_VALUE = 'huchao'
# 2018-09-01 07:37:09.071288
# 获取当前时间
now = datetime.datetime.now()
print(now)
m = hashlib.sha256()
str1 = "%s%s" %(KEY_VALUE,now.strftime('%Y%m%d'))
m.update(str1.encode('utf-8'))
value = m.hexdigest()
print(value)

# 常用标准库
# builtins	内建函数默认加载
# os	操作系统接口
# sys	Python自身的运行环境
# functools	常用的工具
# json	编码和解码 JSON 对象
# logging	记录日志，调试
# multiprocessing	多进程
# threading	多线程
# copy	拷贝
# time	时间
# datetime	日期和时间
# calendar	日历
# hashlib	加密算法
# random	生成随机数
# re	字符串正则匹配
# socket	标准的 BSD Sockets API
# shutil	文件和目录管理
# glob	基于文件通配符搜索

# 常用的扩展库
# requests	使用的是 urllib3，继承了urllib2的所有特性
# urllib	基于http的高层库
# scrapy	爬虫
# beautifulsoup4	HTML/XML的解析器
# celery	分布式任务调度模块
# redis	缓存
# Pillow(PIL)	图像处理
# xlsxwriter	仅写excle功能,支持xlsx
# xlwt	仅写excle功能,支持xls ,2013或更早版office
# xlrd	仅读excle功能
# elasticsearch	全文搜索引擎
# pymysql	数据库连接库
# mongoengine/pymongo	mongodbpython接口
# matplotlib	画图
# numpy/scipy	科学计算
# django/tornado/flask	web框架
# xmltodict	xml 转 dict
# SimpleHTTPServer	简单地HTTP Server,不使用Web框架
# gevent	基于协程的Python网络库
# fabric	系统管理
# pandas	数据处理库
# scikit-learn	机器学习库