# li = [11,32,42,15,12,11]
# li.append(23)
# li.pop(0)
# li.remove(32)
# print(li)

# print(li.count(11))
#
# li.extend([99,123])
# print(li)
#
# li.insert(0,99)
# print(li)
#
# li.sort()
# print(li)
#
# li.sort(reverse=True)
# print(li)
#
# v = li.index(99)
# print(v)
#
# v = li.count(99)
# print(v)
#
# li.reverse()
# print(li)
#
# li.clear()
# print(li)

# dc = {'t':123,'p':234}
# dc.update({'k':33434,'t':1234})
# print(dc)
#
# li = [11,32,42,15,12]
# for i,v in enumerate(li):
#     print(i+1,':',v)
# while True:
#     choice = int(input('input the sn you want:'))
#     if choice < 6:
#         print(li[choice-1])
#     else:
#         print("wrong input!")
#         break

# s = set('hello')
# t = set([123,'2','h','o'])
#
# print(s.intersection(t))
# print(s.union(t))
# print(s.difference(t))
# print(t.difference(s))
#
# s.add('t')
# s.update(['3','f'])
# print(s)
#
# s.pop()
# s.remove('h') #删除元素会报错
# s.discard('h') #删除元素不报错
# print(s)
#
# print(list(t))

# tp = "%(float).2f,%(name)s,%(age)d,%% "%{'float':12.3213,'name':'tt','age':120}
# print(tp)

# func = lambda x,y:x+y
# print(func(1,2))
#
# func = lambda x,y:(x+1,y+1)
# print(func(1,2)[0],func(1,2)[1])

# msg = 'this is a test'
# print(list(map(lambda x:x.upper(),msg)))
# #map函数对列表中的每一个对象进行处理
# #函数式编程中的map函数的使用['T', 'H', 'I', 'S', ' ', 'I', 'S', ' ', 'A', ' ', 'T', 'E', 'S', 'T']
#
# from functools import reduce
# num_l = [1,2,3,4]
# res = reduce(lambda x,y:x*y,num_l,100)
# res1 = reduce(lambda x,y:x+y,num_l,100)
# res2 = reduce(lambda x,y:x+y,range(1,100))
# print(res,res1,res2) #2400 110
# #reduce 函数的使用，把多个值变成一个结果
#
# people = [{'name':'xxx','age':123213},{'name':'zxzxxx','age':12321},{'name':'dayima','age':23}]
# print(list(filter(lambda x:x['age'] < 24,people)))
# #filter函数遍历列表元素，只留下符合判断条件的列表元素

# print(list(zip('12345','abcde')))
# #把两个序列按照一一对应关系合在一起[('1', 'a'), ('2', 'b'), ('3', 'c'), ('4', 'd'), ('5', 'e')]
#
# mydic = {'age1':12,'age2':23,'age3':45}
# print(max(zip(mydic.keys(),mydic.values())))
# print(min(zip(mydic.keys(),mydic.values())))
# print(sorted(zip(mydic.keys(),mydic.values())))
#
# peo = [{'name':'xzx','age':23},{'name':'xx','age':33},{'name':'xxq','age':123}]
# print(max(peo,key=lambda dic:dic['age']))
# #max比较字典的某元素，返回该元素对应的整体
#
# l = [1,2,3,4,5,6,1,32,12,43,12,5]
# print(sorted(l))
# print(sorted(peo,key=lambda dic:dic['age']))
# #排序的高级用法
#
# f = open('seek.txt','rb')
# f.seek(3,0) #从文件开始光标移动三个字节
# f.seek(3,1) #从光标上一次的位置向后移动三个字节
# f.seek(-3.2) #从文件最后向前移动三个字节
# f.tell() #获取当前光标所在的位置是第几个字节

# res = [i for i in range(19) if i % 2 == 0] #列表生成式，所有元素都存在内存中，占用内存资源较多
# ites = (i for i in range(19) if i % 2 == 0) #生成器表达式，生成可迭代对象，调用一次__next()__方法，生成一个值，返回一个值
# print(sum(res))
# print(sum(ites))

# def test_yield():
#     for i in range(8):
#         yield i
#
# t = test_yield()
# for i in t:
#     print(i)


# import time
#
# print(time.localtime(time.time())) #时间戳转结构化时间
# print(time.localtime(time.time()).tm_year)
# print(time.mktime(time.localtime())) #结构化时间转时间戳
#
# print(time.strftime("%Y-%m-%d:%X")) #结构化时间转字符串时间
# print(time.strptime("2018-06-11:19:56:36","%Y-%m-%d:%X")) #时间字符转结构化时间
# print(time.strptime("2018-06-11:19:56:36","%Y-%m-%d:%X").tm_mon)
#
# print(time.asctime()) #将结构化时间转化为固定的字符串时间
# print(time.ctime()) #将时间戳转化为固定的字符串时间


# import random
#
# print(random.random()) #0.49762882621095283
#
# print(random.randint(1,3)) #1 1-3随机取一个
# print(random.randrange(1,3)) #2 1-2随机取一个
#
# print(random.choice([1,2,11])) #1 在列表中随机取一个
# print(random.sample([1,2,11],2)) #[2, 11] 取两个列表中的元素组成新的列表


# import math
# res = math.sqrt( 16 ) #求一个数的平方根
# if str(res).split('.')[1] == '0':
#     print('it is an instance of integer')
# else:
#     print('it is a float')
# print(res)

################### with and as

# class Foo(object):
#     def __init__(self,name):
#         self.name = name
#
#     def __enter__(self): #with语句调用的方法
#         print("in enter")
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb): #执行完with下的语句，或执行中异常时执行
#         print("exited")
#         return True #吞下异常，不终止程序的执行，但是with下的语句就不再执行
#
# with Foo('test') as f:
#     print(f.name)

# print('1' in '?2+?=?3')
# print('?2+?=?3'.count('?'))


################### 套接字编程流程（TCP）

# import socket
#
# data= "hello world!"
#
# svr = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #服务器端
# svr.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #如果重启服务器时，出现地址已经在使用的错误，设置该命令
# svr.bind('127.0.0.1',8080)
# svr.listen(5)
# conn,addr = svr.accept()
# conn.recv(1024)
# conn.send(data.encode())
# svr.close()
#
#
# cli = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #客户端
# cli.connect('127.0.0.1',8080)
# cli.send(data.encode())
# cli.recv(1024)
# cli.close()
#
#
# ################# 套接字编程流程（UDP）UDP
#
# import socket
#
# data= "hello world!"
# svr = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #服务器端
# svr.bind('127.0.0.1',8080)
# while True:
#     redata,addr = svr.recvfrom(1024)
#     print(redata,addr)
#     svr.sendto(redata.upper(),addr)
#
#
# cli = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #客户端
# while True:
#     msg = input(">>>: ").strip()
#     cli.sendto(data.encode(),('127.0.0.1',8080))
#     resdata,addr = cli.recvfrom(1024)
#     print(resdata.addr)
#
#
# ######################## subprocess模块
#
# import subprocess
#
# res = subprocess.Popen('ifconfig -a',shell=True,
#                        stderr=subprocess.PIPE,
#                        stdin=subprocess.PIPE,
#                        stdout=subprocess.PIPE)
# err = res.stderr.read()
# if err:
#     std_res = err
# else:
#     std_res = res.stdout.read()


############################ 使用os模块递归显示当前目录下的所有文件和文件夹

import os
#
# def dis_dir(dirname,j=0):
#     i = len(os.path.basename(dirname))+3
#     v = i + j
#     print(" "*j,"<"+os.path.basename(dirname)+">:")
#     for file_name in os.listdir(dirname): # list出来的文件和文件夹都是相对路径
#         file_name = os.path.join(dirname, file_name) # 拼接出一个绝对路径
#         if os.path.isdir(file_name): # 只能判断完全路径是否为文件夹，相对路径不行
#             dis_dir(file_name,v)
#         else:
#             print(" "*v,os.path.basename(file_name))
#
# dis_dir(os.getcwd())

# os.makedirs('testdir/testdir2') # 一次创建多层目录

################################ 文件下载进度显示功能实现

# import sys,time
#
# def dis_ppercent(transed_data_size, total_data_size):
#     '''
#     显示文件传输进度的功能模块
#     :param transed_data_size:
#     :param total_data_size:
#     :return:
#     '''
#     percentage = int(float(transed_data_size) / float(total_data_size) * 100)
#     sys.stdout.write("%s%% %s\r" % (percentage, '#' * percentage))
#     sys.stdout.flush()
#     time.sleep(0.2)
#
# for i in range(1,101):
#     dis_ppercent(i,100)

# import gevent,time,requests
#
# start = time.time()
#
# def f(url):
#     print('get: %s'%url)
#     resp = requests.get(url) # 生成一个获取http响应内容的对象，并获取其url的内容
#     data = resp.text # 获取url内的文本内容
#     print('%d received from %s'%(len(data),url))
#
# gevent.joinall([
#     gevent.spawn(f,'https://www.bilibili.com/'),
#     gevent.spawn(f,'http://www.ttmeiju.vip/'),
#     gevent.spawn(f,'https://www.jd.com/'),
#     gevent.spawn(f,'https://sub.kamigami.org/'),
#     gevent.spawn(f,'http://www.xiaohuar.com/')
# ]) # 使用协程，完成获取多个网页内容的操作，只要其中一个任务在等待I/O完成，程序就运行下一个获取网页的操作
#
# # # 串行执行获取网页的操作，可以和协程执行所需要的时间对比
# # f('https://www.bilibili.com/')
# # f('http://www.ttmeiju.vip/')
# # f('https://www.jd.com/')
# # f('https://sub.kamigami.org/')
# # f('http://www.xiaohuar.com/')
#
# stop = time.time()
#
# print('comsumed time: ',stop-start)

################################ 数据库连接模块pymysql的使用(操作原生的SQL语句)

# import pymysql
#
# conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='redhat',db='mytest')
# # 连接远程数据库
# curser = conn.cursor() # 获取游标
# res = curser.execute("show tables") # 执行原生的SQL语句，默认只是返回结果的行数
#
# one = curser.fetchone() # 获取第一条查询结果
# many = curser.fetchmany(3) # 获取前三条查询结果
# fetall = curser.fetchall() # 获取所有的查询结果
#
# curser.scroll(-1,mode='relative') # 光标向上移动一位
# curser.scroll(1,mode='absolue') # 光标移动到第一位
#
# conn.commit() # 提交要执行的命令
# conn.rollback() # 回滚到事务的开始阶段
#
# curser.close() # 关闭游标
# conn.close() # 关闭到数据库的远程连接

################################ 字符串类型判断回忆

# s = '    '
# if s.isspace(): # 判断字符串是不是空格
#     print('space')
# if s.isdigit():
#     print('digit')
# if s.isidentifier(): # 判断字符串是不是以字母开头的
#     print('identifier')

# import os,subprocess
#
# # res = os.system("ipconfig")
# # print(res)
#
# res = subprocess.getoutput("shutdown")
# print(res)


################################ 字符串格式化输出的几种方式

# class TCL(object):
#
#     def __init__(self,*args,**kwargs):
#         self.name = args[0]
#         self.gender = args[1]
#
#     def print_info(self):
#         print(self.name,self.gender)
#
#     def __str__(self):
#         return self.name
#
# a = 123
# b = "test"
# testobj = TCL("zx","dajiji")
# test_dic = {"a":a,"b":b,"obj":testobj}
# test_list = [a,b,testobj]
#
# # 字符串格式化，使用f前缀就可以完成format函数的功能
# print(f"{a},{b},{testobj}")
#
# print("{a},{b},{obj}".format(a=a,b=b,obj=testobj))
# print("{a},{b},{obj}".format(**test_dic))
#
# print("{0},{1},{2}".format(a,b,testobj))
# print("{0},{1},{2},{0}".format(*test_list))
#
# print("%s,%s,%s"%(a,b,testobj))

# num = [1,6,6,3,6,2,10,2,100]
# num_set = set(num)
# num_set.remove(6)
# print(sorted(list(num_set)))

# num = [1,1,1,22,22,3]
#
# num_dic = {}
#
# for i in num:
#     if i not in num_dic:
#         num_dic[i] = 1
#     else:
#         num_dic[i] += 1
#
# num_new = []
#
# for k,v in num_dic.items():
#     if v >= 2:
#         j = 1
#         while j <= 2:
#             num_new.append(k)
#             j += 1
#     else:
#         num_new.append(k)
#
# print(num_new)


#################### 使用字符串导入模块 #####################

# import importlib
#
# path = "E:\PycharmProjects\codewars\send_message.py"
# fullpath_name = path.split('.')[0]
# module_name = fullpath_name.split('\\')[-1]
#
# # 注意module_name必须是文件的名字，但是不能带.py
# file_obj = importlib.import_module(module_name)
#
# cls = getattr(file_obj,"My_Twilio_SMS")
# obj = cls()
#
# message_body = "ooooooooooo"
# # twilio分配的发送短信用的号码
# sender_num = "+14693457649"
# # 接收短信的用户号码
# # receiver_num_list = ["+8618687001736", "+8618687027119", "+8613529209726","+8618552064396"]
# receiver_num_list = ["+8618552064396"]
#
# # 创建并发送短信
# # message = client.messages.create(to=receiver_num,from_=sender_num,body=message_body)
# for receiver_num in receiver_num_list:
#     obj.my_send_SMS(message_body, sender_num, receiver_num)


################ 面试练习题 ################

# print(sum(range(1,101)))


# a = 100
#
# def change_a():
#     global a
#     a += 1
#
# change_a()
# print(a)


# ori_li = [2,4,6,8]
#
# res_li = list(map(lambda x:x*x,ori_li))
# print(res_li)


# def mydecfunc(func):
#     ori_pass = 'zx123'
#     def inner(*args,**kwargs):
#         password = input('please input password: ')
#         if password == ori_pass:
#             return func(*args,**kwargs)
#         else:
#             return "wrong password!"
#     return inner
#
# @mydecfunc
# def myfunc(num):
#     return num**2
#
# print(myfunc(100))


# import re
#
# reg_pre = r'(?=.*)-(.*)-(?=.*)'
# # reg_pre = r'(.*)-(.*)-(.*)'
# myre = re.compile(reg_pre)
# res = myre.findall('123-321-123213')
# print(res)
#
# reg_pre1 = r'-(?P<test>.*)-'
# myre = re.compile(reg_pre1)
# res1 = myre.search('123-321-123213')
# print(res1.group('test'))

# sum = lambda a,b:a*b
# print(sum(2,3))


########### 统计字符串中每个字母出现的次数 ###########

# from collections import Counter
# a = 'wqeqwefdafwerrqweqwe'
# res = Counter(a)
# print(res)
# # Counter({'w': 5, 'e': 5, 'q': 4, 'f': 2, 'r': 2, 'd': 1, 'a': 1})


########### 使用filter函数过滤列表 ###########

# a = [1,2,3,4,5,6,7,8,9,10]
#
# def judge(num):
#     if num%2 == 0:
#         return False
#     else:
#         return True
#
# res_li = list(filter(judge,a))
#
# print(res_li)
# # [1, 3, 5, 7, 9]


########### 列表生成式 ###########

# a = [1,2,3,4,5,6,7,8,9,10]
# res_li = [i for i in a if i%2!=0 ]
# print(res_li)

# a = [1,2,3]
# b = [4,5,6]
# a.extend(b)
# c = sorted(a,reverse=True)
# print(c)


########### 将2维列表转换为1维 ###########

# a = [[1,2],[3,4],[5,6],[7,8]]
# flat_a = [j for i in a for j in i ]
# print(flat_a)


########### 替换指定字符串中的所有符合匹配规则的字符为指定的字符 ###########

# import re
# a = "12000 this is a 10022 test for number 98"
# res = re.sub(r"\d+","100",a)
# print(res)
# # 100 this is a 100 test for number 100


########### 使用zip函数和生成器 ###########

# a = [1,2,3,4]
# b = ["a","b","c","d"]
#
# res = (z for z in zip(a,b))
# for i in res:
#     print(i)
#
# # (1, 'a')
# # (2, 'b')
# # (3, 'c')
# # (4, 'd')


########### 从小到达排序列表 ###########

# li = [2,4,7,6,9,8,1,1]
# res_li = []
#
# def find_min(li):
#     min_v = li[0]
#     if len(li) > 1:
#         for j in li[1:]:
#             if min_v > j:
#                 min_v = j
#     return min_v
#
# while li:
#     min_v = find_min(li)
#     res_li.append(min_v)
#     li.remove(min_v)
#
# print(res_li)
# [1, 1, 2, 4, 6, 7, 8, 9]


# import requests,re,json
# from bs4 import BeautifulSoup
#
# response = requests.get(
#     url="https://www.bilibili.com/video/av37026918/?spm_id_from=333.334.b_686f6d655f706f70756c6172697a65.4",
#     headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3521.2 Safari/537.36"}
# )
#
# response.encoding = response.apparent_encoding
#
# tmp = re.findall(r'\<script\>window\.__playinfo__=(.*?)\</script\>',response.text)[0]
# tmp = json.loads(tmp)
#
# video_url = None
# for key,val in tmp["durl"][0].items():
#     if key =='url':
#         video_url = val
#
#
# # print(tmp)
# print(video_url)
# r1 = requests.get(
#     url=video_url,
#     headers={
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3521.2 Safari/537.36",
#     },
#     stream=True,
#     verify=False
# )
#
# with open("bilibili.mp4",'wb') as f:
#     f.write(r1.content)


########### 基本的函数装饰器 ###########

# def dec(func):
#     def inner(*args,**kwargs):
#         print("in the inner")
#         return func(args[0])
#     return inner
#
# @dec
# # 先把ori_func赋值给dec的func变量，
# # 再把ori_func的参数传递到inner的参数中，
# # 最后把inner赋值给ori_func
# def ori_func(num):
#     return num+1
#
# ori_func(100)


########### 列表切片总结(永远都是取的左闭，右开区间) ###########


# test_li = [1,2,3,4,5,6,7]
#
# print(test_li[:-3]) # [1, 2, 3, 4]
# print(test_li[-3:]) # [5, 6, 7]
# print(test_li[0:2]) # [1, 2]
# print(test_li[:2]) # [1, 2]
# print(test_li[2:]) # [3, 4, 5, 6, 7]
# print(test_li[2:-1]) # [3, 4, 5, 6]
# print(test_li[::-1]) # [7, 6, 5, 4, 3, 2, 1]


########### 类的几个特殊方法的使用 ###########


# class MyItemTest(object):
#
#     def __init__(self):
#         self.userinfo = {'name':'zx','age':34}
#
#     def __call__(self, *args, **kwargs):
#         print(self.userinfo)
#
#     def __getitem__(self, item):
#         return self.userinfo[item]
#
#     def __setitem__(self, key, value):
#         self.userinfo[key] = value
#
#     def __delitem__(self, key):
#         del self.userinfo[key]
#
#
# if __name__ == '__main__':
#
#     myobj = MyItemTest()
#
#     # 调用__setitem__方法
#     myobj['gender'] = 'Male'
#     myobj()
#
#     # 调用__getitem__方法
#     res = myobj['name']
#     print(res)
#
#     # 调用__delitem__方法
#     del myobj['gender']
#     myobj()
#
#     # 在类对象后加上小括号，就可以调用__call__方法
#     myobj() # in the call function


########### 遍历列表删除元素的正确方式 ###########

# import random
#
# test_li = list(range(10))
# random.shuffle(test_li)
# print(test_li)
#
# i = 0
# while i < len(test_li):
#     if test_li[i] >= 5:
#         # del test_li[i]
#         test_li.remove(test_li[i])
#         continue
#     i += 1
#
# print(test_li)


########### 字符串转字典 ###########

# passages = '''
#     this is a test
#     they are my best
#     he fucked you twice
# '''
#
# tmp_li = passages.split('\n')
# p_li = []
#
# for i in tmp_li:
#     if i:
#         p_li.extend(i.split())
#
# print(p_li)
#
# p_dict = {}
# tmpli = []
# tmp_v = ''
# for i,v in enumerate(p_li):
#     if i % 4 == 0:
#         tmp_v = v
#     else:
#         tmpli.append(v)
#     if len(tmpli) == 3:
#         p_dict[tmp_v] = ' '.join(tmpli)
#         tmpli.clear()
#
# print(p_dict)


########### 带参数的装饰器函数 ###########

# def outter(flag):
#     def wrapper(func):
#         def inner(*args,**kwargs):
#             if flag:
#                 print('before func')
#                 res = func(*args,**kwargs)
#                 print('after func')
#                 return res
#             else:
#                 print('do nothing')
#                 return func(*args,**kwargs)
#         return inner
#     return wrapper
#
# @outter(True)
# def bigger1(a,b):
#     return a if a > b else b
#
# @outter(False)
# def bigger2(a,b):
#     return a if a > b else b
#
# print(bigger1(1,4))
# print(bigger2(3,55))


########### 多重装饰器 ###########

# def wrapper1(func):
#     def inner1(*args,**kwargs):
#         print('before wrapper1 in func %s'%func.__name__)
#         res = func(*args,**kwargs)
#         print('after wrapper1 in func %s' % func.__name__)
#         return res
#     return inner1
#
# def wrapper2(func):
#     def inner2(*args,**kwargs):
#         print('before wrapper2 in func %s'%func.__name__)
#         res = func(*args,**kwargs)
#         print('after wrapper2 in func %s' % func.__name__)
#         return res
#     return inner2
#
# @wrapper1
# @wrapper2
# def bigger(a,b):
#     return a if a > b else b
#
# print(bigger(100,23))


########### 生成器中send方法的使用示例 ###########

# def init_gen(func):
#     def inner(*args,**kwargs):
#         genobj = func(*args,**kwargs)
#         genobj.__next__()
#         return genobj
#     return inner
#
# @init_gen
# def myavggen():
#     sum = 0
#     count = 0
#     avg = 0
#     while True:
#         num = yield avg
#         sum += num
#         count += 1
#         avg = sum/count
#
# genobj = myavggen()
# genobj.send(10)
# genobj.send(12)
# res = genobj.send(32)
# print(res)


########### 让生成器每次返回可迭代对象中的一个值 ###########

# def mygenfrom():
#     li1 = [1,2,3,4,5,6]
#     li2 = ['a','b','c','d','e']
#     yield from li1
#     yield from li2
#
# yieldfromobj = mygenfrom()
# for i in yieldfromobj:
#     print(i)


# li = [[1,2,3,4,5],['a','b','c','d','e']]
# mydict = {li[0][i]:li[1][i] for i in range(len(li[0]))}
# print(mydict)
#
# myli = [i for item in li for i in item]
# print(myli)


########### print函数使用进阶  ###########

# print('test',end=' ')
# print('test2','test3','test4',sep='!')

# import time
# for i in range(0,101,2):
#     time.sleep(0.1)
#     count = i//4
#     present = '\r%s%%:%s\n'%(i,'*'*count) if i == 100 else '\r%s%%:%s'%(i,'*'*count)
#     print(present,flush=True,end='')

# f = open('temp.txt','w',encoding='utf-8')
# print('this is a test',file=f) # 将打印的东西输出到文件
# f.close()


########### max，min，reversed，sorted，map，filter,zip  ###########

# test_li = [10,-2,3,-45,12,11,-23]
# test_li1 = [110,-23,31,-245,121,131,-235]
# test_dic = {'a':1,'b':4,'c':3}

# res1 = max(test_li,key=abs)
# print(res1)
#
# res2 = min(test_li,key=abs)
# print(res2)
#
# res3 = reversed(test_li)
# print(list(res3))
#
# res4 = sorted(test_li,key=abs)
# res5 = sorted(test_li,reverse=True)
# print(res4,'\n',res5)
# res9 = sorted(test_dic,key=lambda k:test_dic[k])
# print(res9)
#
# res6 = zip(test_li,test_li1)
# print(list(res6))
#
# res7 = map(abs,test_li1)
# print(list(res7))
#
# res8 = filter(lambda x:x**3>10,test_li)
# print(list(res8))
#
# test_tup = (('a','b'),('c','d'))
# mytup_li = list(zip(test_tup[0],test_tup[1]))
# dic_li = list(map(lambda item:{item[0]:item[1]},mytup_li))
# print(dic_li)

# td = {}
# tt = map(lambda key:{test_dic[key]:key},test_dic)
# for i in tt:
#     td.update(i)
#
# print(td)


import re

# # 给正则表达式分组命令之后，之后可以使用group(分组名字)取得字符串中匹配到的值
# info = re.compile(r"^name:(?P<name>.*?),gender:(?P<gender>.*?),age:(?P<age>\d+)$")
# res = info.search("name:zx,gender:male,age:23")
#
# print(res.group('name'))
# print(res.group('gender'))
# print(res.group('age'))

# res = re.search(r"\([^()]+\)","((1+2+(4+3))+(2+1))")
# print(res.group().strip("()"))


# from collections import OrderedDict,defaultdict
#
# d = OrderedDict([('a',1),('b',1),('c',1)])
# print(d['c'])
# for k,v in d.items():
#     print(k,v)
#
# d1 = defaultdict(lambda :5)
# print(d1['k'])
#
# import queue
#
# myq = queue.Queue(maxsize=10)
# myq.put(10)
# myq.put(20)
# myq.put(23)
# myq.put(24)
# # myq.put_nowait(12)
# print(myq.qsize())
# myq.get()
# myq.get()
# myq.get()
# myq.get()
# # myq.get()
# myq.get_nowait()


# import time
#
# print(time.localtime())
# print(time.strftime("%Y-%d %X"))
# print(time.time())
#
# mystr_time = time.strftime("%Y-%d %X")
# my_struct_time = time.strptime(mystr_time,"%Y-%d %X")
# my_num_time = time.mktime(my_struct_time)
#
# print(mystr_time)
# print(my_struct_time)
# print(my_num_time)


# import sys
#
# print(sys.path)
# print(sys.platform)
# print(sys.version)

# import os
# print(os.system('dir'))

################# 显示多层菜单

# menu = {'1':{'12':{'113':{}}},'2':{'22':{'223':{}}},'3':{'32':{'333':{}}}}

# li = [menu]
# while li:
#     for key in li[-1].keys():
#         print(key)
#     k = input('input>>>').strip()
#     if k in li[-1].keys() and li[-1][k]:
#         li.append(li[-1][k])
#     elif k == 'b':
#         li.pop()
#     elif k == 'q':
#         break
#     else:
#         continue

# def my_three_layer(menu_dic):
#     while True:
#         for key in menu_dic:
#             print(key)
#         k = input('input>>>').strip()
#         if k == 'b' or k == 'q':return k
#         if k in menu_dic.keys() and menu_dic[k]:
#             res = my_three_layer(menu_dic[k])
#             if res == 'q':return
#
# my_three_layer(menu)


# class TestClassDec(object):
#     class_attr = 'class_1'
#
#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender
#
#     @staticmethod
#     def login():
#         name = input('name>>>').strip()
#         passwd = input('passwd>>>').strip()
#         if name == 'root' and passwd == '123':
#             gender = input('gender>>>').strip()
#             myobj = TestClassDec(name,gender)
#         else:
#             print('wrong name or passwd')
#
#     @classmethod
#     def change_classattr(cls,new_value):
#         cls.class_attr = new_value
#
#     @property
#     def mypro(self):
#         return self.name + self.gender


# # 当这个方法的操作只涉及类的静态属性的时候 就应该使用classmethod来装饰这个方法
# class Goods(object):
#
#     __discount = 0.8
#
#     def __init__(self,name,price):
#         self.name = name
#         self.__price = price
#
#     # 对象可以使用调用属性的方式,调用该装饰器装饰的函数，而不用加()
#     @property
#     def price(self):
#         return self.__price * Goods.__discount
#
#     # 把一个方法 变成一个类中的方法，这个方法就直接可以被类调用，不需要依托任何对象
#     @classmethod
#     def change_discount(cls,new_discount):  # 修改折扣
#         cls.__discount = new_discount
#
# apple = Goods('苹果',5)
# print(apple.price)
# Goods.change_discount(0.5)   # Goods.change_discount(Goods)
# print(apple.price)


# # 在完全面向对象的程序中，
# # 如果一个函数，既和对象没有关系，也和类没有关系，
# # 那么就用staticmethod将这个函数变成一个静态方法
# class Login:
#     def __init__(self,name,password):
#         self.name = name
#         self.pwd = password
#
#     def login(self):
#         print(self.name,':',self.pwd)
#
#     # 静态方法，没有任何的默认参数，通过类和对象都可以调用
#     @staticmethod
#     def get_usr_pwd():
#         usr = input('用户名 ：')
#         pwd = input('密码 ：')
#         return Login(usr,pwd)
#
# lobj = Login.get_usr_pwd()
# lobj.login()
#
# lobj1 = Login('123','1233')
# lobj1.login()
#
# lobj2 = lobj1.get_usr_pwd()
# lobj2.login()

# 属性 查看 修改 删除
# class Person:
#     def __init__(self,name):
#         self.__name = name
#         self.price = 20
#
#     # 使用调用属性的方式，运行函数
#     @property
#     def name(self):
#         return self.__name
#
#     # 删除对象的某个属性
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     # 修改对象的某个属性的值
#     @name.setter
#     def name(self,new_name):
#         self.__name = new_name
#
# ctobj = Person('ct')
# ctobj.name = 'newName'
# print(ctobj.name)
#
# del ctobj.name
# print(ctobj.name)


############# 使用正则表达式完成字符串算式的计算 #############
# import re
#
# def format_exp(exp):
#     exp = exp.replace('--','+')
#     exp = exp.replace('+-','-')
#     exp = exp.replace('-+','-')
#     return exp
#
# def cal_md(exp):
#     while True:
#         ret = re.search(r'\d+\.?\d*[*/]-?\d+\.?\d*',exp)
#         if ret:
#             res = ret.group()
#             if '*' in res:
#                 a,b = res.split('*')
#                 cal_res = float(a) * float(b)
#                 exp = exp.replace(res,str(cal_res))
#                 # exp = format_exp(exp)
#             if '/' in res:
#                 a,b = res.split('/')
#                 cal_res = float(a) / float(b)
#                 exp = exp.replace(res,str(cal_res))
#                 # exp = format_exp(exp)
#         else:
#             exp = format_exp(exp)
#             return exp
#
# def cal_pr(exp):
#     res_li = re.findall(r'-?\d+\.?\d*', exp)
#     sum = 0
#     for i in res_li:
#         sum += float(i)
#     return str(sum)
#
# def find_bra(exp):
#     while True:
#         get_exp_in_brac = re.search(r'\([^()]+\)',exp)
#         if get_exp_in_brac:
#             exp_res = get_exp_in_brac.group()
#             exp_without_brac = exp_res.strip('()')
#             exp_with_out_md = cal_md(exp_without_brac)
#             exp_final = cal_pr(exp_with_out_md)
#             exp = exp.replace(exp_res,exp_final)
#         else:
#             exp_with_out_md = cal_md(exp)
#             exp_final = cal_pr(exp_with_out_md)
#             return exp_final
#
# calculation = '3-(-4+2*(-2*3+(-100/-10)))'
# res = find_bra(calculation)
# print(res)
#
# print(eval(calculation))

# def cal_pr(exp):
#     while True:
#         ret = re.search(r'-?\d+\.?\d*[+-]-?\d+\.?\d*',exp)
#         if ret:
#             res = ret.group()
#             if '+' in res:
#                 a,b = res.split('+')
#                 cal_res = float(a) + float(b)
#                 exp = exp.replace(res,str(cal_res))
#             if not res.startswith('-') and '-' in res:
#                 a,b = res.split('-')
#                 cal_res = float(a) - float(b)
#                 exp = exp.replace(res,str(cal_res))
#             else:
#                 a,b = re.findall(r'-?\d+\.?\d*',res)
#                 cal_res = float(a) + float(b)
#                 exp = exp.replace(res,str(cal_res))
#         else:
#             return exp
#
# cal_exp = '-5+4-1+3'
# # cal_exp = '-5-4'
# print(cal_pr(cal_exp))


############# 类的内置方法 #############
# class A(object):
#
#     grade = 'No.1'
#     __key = "secret"
#
#     def __init__(self,name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     @classmethod
#     def show_seckey(cls):
#         return A.__key
#
#     def __str__(self):
#         return "obj name is %s"%self.__name
#
#     def __repr__(self):
#         return "obj name is not %r"%self.__name
#
#     def __call__(self, *args, **kwargs):
#         print('run call function')
#
#     def __del__(self):
#         print("run del function")

# a = A("zx")
# a()
# print(a)
# a.age = 34
# print(a.age)
# del a.age
# print(a.age)

# if hasattr(a,'get_name'):
#     func = getattr(a,'get_name')
#     print(func())
#
# if hasattr(a,'age'):
#     age = getattr(a,'age')
#     print(age)
#
# if hasattr(A,'grade'):
#     aat = getattr(A,'grade')
#     print(aat)
#
# if hasattr(A,'show_seckey'):
#     func = getattr(A,'show_seckey')
#     print(func())

# import sys
# if hasattr(sys.modules[__name__],"A"):
#     ClassMod = getattr(sys.modules[__name__],"A")
#     a = ClassMod('zxdg')
#     print(a)

# import os,sys
# sys.path.append(os.path.dirname(os.getcwd()))
# from codewars import cake
# if hasattr(cake,"cakes"):
#     func = getattr(cake,"cakes")
#     func()

# setattr(a,"pwd","12306")
# print(a.pwd)
#
# setattr(A,"def_pwd","1230606")
# print(A.def_pwd)
#
# print(a.age)
# delattr(a,"age")
# print(a.age)

# class A(object):
#
#     __objected = False
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__objected:
#             return cls.__objected
#         cls.__objected = object.__new__(cls)
#         return cls.__objected
#
# a = A('zx',32)
# b = A('tutu',34)
# print(a.name,a)
# print(b.name,b)

# 常用内置方法的基础使用
# class A(object):
#
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def __getitem__(self, item):
#         return self.__dict__[item]
#
#     def __setitem__(self, key, value):
#         self.__dict__[key] = value
#
#     def __delitem__(self, key):
#         del self.__dict__[key]
#
#     def __eq__(self, other):
#         if self.name == other.name and self.gender == other.gender:
#             return True
#         return False
#
#     def __hash__(self):
#         return hash(self.name+self.gender)
#
#     def __len__(self):
#         return len(self.__dict__.keys())
#
# a = A('zx',23,'male')
# b = A('zx',28,'male2')
# print(a == b)
# print(set((a,b)))
# a['hobit'] = 'female'
# print(a['hobit'])
# print(a.hobit)
# print(len(a))
# del a['age']
# print(a.age)

# logging模块的基础使用
# import logging
#
# my_logger = logging.getLogger('mylog')
#
# log_fmt1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s [line:%(lineno)d] : %(message)s')
# log_fmt2 = logging.Formatter('[%(lineno)d] %(asctime)s %(message)s')
#
# file_handler = logging.FileHandler('mylogfile.txt',encoding='utf-8')
# stdn_handler = logging.StreamHandler()
#
# file_handler.setFormatter(log_fmt1)
# stdn_handler.setFormatter(log_fmt2)
#
# # file_handler.setLevel(logging.DEBUG)
# # stdn_handler.setLevel(logging.WARNING)
#
# my_logger.addHandler(file_handler)
# my_logger.addHandler(stdn_handler)
#
# my_logger.setLevel(logging.INFO)
#
# my_logger.debug('debug level information')
# my_logger.info('info level information')
# my_logger.warning('warning level information')
# my_logger.error('error level information')
# my_logger.critical('critical level information')

# import configparser
#
# my_config = configparser.ConfigParser()
#
# # 必须要有"DEFAULT"字段
# my_config["DEFAULT"] = {'ServerAliveInterval': '45',
#                         'Compression': 'yes',
#                         'CompressionLevel': '9',
#                         'ForwardX11':'yes'
#                         }
# my_config['httpd'] = {'User':'hg'}
# my_config['nginx'] = {'Host Port':'50022','ForwardX11':'no'}
#
# f = open('config.ini','w')
# my_config.write(f)
# f.close()

# import configparser
#
# config = configparser.ConfigParser()
#
# config.read('config.ini',encoding='utf-8')
#
# print('bitbucket.org' in config)
# print(config.sections())
#
# print(config['DEFAULT'])
# print(config['DEFAULT']['CompressionLevel'])
# print(config.get('DEFAULT','CompressionLevel'))
#
# print(config.options('nginx'))
# print(config.items('DEFAULT'))
#
# for i in config:
#     print(i)
#
# for i in config['DEFAULT']:
#     print(i)
#
# # default字段的值属于下面的所有字段
# for k,v in config['nginx'].items():
#     print(k,v)

# import configparser
#
# config = configparser.ConfigParser()
#
# config.read('config.ini',encoding='utf-8')
#
# config.add_section('tomcat')
# config.remove_option('DEFAULT','ForwardX11')
# config.remove_section('nginx')
#
# config.set('tomcat','listen','8080')
# config.set('tomcat','ip','*')
#
# f = open('new_config.ini', "w")
# config.write(f)
# f.close()
#
# # with open('config.ini','w',encoding='utf-8') as f:
# #     with open('new_config.ini','r',encoding='utf-8') as f1:
# #         for line in f1:
# #             f.write(line)
#
# import os
# os.remove('config.ini')
# os.rename('new_config.ini','config.ini')
# print(os.stat('config.ini'))

# 内置预共享密钥加密模块使用
# import hmac
#
# h_key = b'123abc'
# # 使用预共享密钥和bytes类型的字符串，生成加密信息
# h_res = hmac.new(h_key,'hello'.encode('utf-8'))
# # 获取加密之后的bytes类型的字符串
# print(h_res.digest())


# # pymysql的基础使用
# import pymysql
#
# conn = pymysql.connect(
#     host='10.1.1.128',
#     port=3306,
#     user='zx',
#     passwd='redhat',
#     db='test')
#
# cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
# # cur = conn.cursor()
#
# cur.execute('show tables;')
# res_li = cur.fetchall()
# print(res_li)
#
# # sql = "INSERT INTO customers (NAME, gender, occupation) VALUES ('danaizi', 'Female', 'huoji');"
# # cur.execute(sql)
# # conn.commit()
# # print(cur.lastrowid)
#
# cur.execute('select * from customers')
# res_li = cur.fetchall()
# print(res_li)
#
# cur.callproc('p1',(12,2))
# r1 = cur.fetchall()
# print("***",r1)
#
# cur.execute("select @_p1_1")
# r2 = cur.fetchall()
# print("***",r2)
#
# name = input('name:').strip()
# passwd = input('passwd:').strip()
# sql = 'select * from user where name=%s and passwd=%s'%(name,passwd)
# cur.execute(sql)
# res = cur.fetchone()
# if res:
#     print('logined')
# else:
#     print('wrong name or passwd')
#
# cur.close()
# conn.close()

# test_txt = "this is|a test|for your|mama"
# print(test_txt.split("|",2))


############# SQLalchemy #############

# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column,Integer,String,ForeignKey,UniqueConstraint,Index,CHAR,VARCHAR
# from sqlalchemy.orm import sessionmaker,relationship
# from sqlalchemy import create_engine
#
# Base = declarative_base()
#
# class UserType(Base):
#     __tablename__ = 'usertype'
#     id = Column(Integer,primary_key=True,autoincrement=True)
#     catagory = Column(VARCHAR(32),nullable=True,index=True)
#
# class Users(Base):
#     __tablename__ = 'users'
#     id = Column(Integer,primary_key=True,autoincrement=True)
#     name = Column(VARCHAR(32),nullable=True,index=True)
#     email = Column(VARCHAR(32),unique=True)
#     user_type_id = Column(Integer,ForeignKey("usertype.id"))
#
#     user_type = relationship("UserType",backref='users')

    # __table_args__ = (
    #     UniqueConstraint('id','name',name='uix_id_name'),
    #     Index('in_n_ex','name','email'),
    # )

# def create_db():
#     engine = create_engine("mysql+pymysql://zx:redhat@10.1.1.128:3306/test?charset=utf8", max_overflow=5)
#     Base.metadata.create_all(engine)
#
# def drop_db():
#     engine = create_engine("mysql+pymysql://zx:redhat@10.1.1.128:3306/test?charset=utf8", max_overflow=5)
#     Base.metadata.drop_all(engine)
#
# engine = create_engine("mysql+pymysql://zx:redhat@10.1.1.128:3306/test?charset=utf8", max_overflow=5)
# # Base.metadata.create_all(engine)
#
# Session = sessionmaker(bind=engine)
# session = Session()

# obj_li = [
#     UserType(catagory='DIAMOND_user'),
#     UserType(catagory='GOLD_user'),
#     UserType(catagory='SILVER_user')
# ]
# session.add_all(obj_li)
#
# obj = UserType(catagory='BLACKGOLD_user')
# session.add(obj)

# user_type_list = session.query(UserType).all()
# # print(user_type_list)
# for row in user_type_list:
#     print(row.id,row.catagory)

# type_li = session.query(UserType).filter(UserType.id == 10)
# for row in type_li:
#     print(row.id,row.catagory,row.users)
#     for i in row.users:
#         print(i.name)

# users_li = session.query(Users.name).join(UserType,isouter=True).filter(UserType.catagory=='BLACKGOLD_user')
# for row in users_li:
#     print(row)

# q2 = session.query(Users.name).filter(Users.user_type_id.in_(session.query(UserType.id).filter(UserType.id > 9))).all()
# print(q2)

# result = session.query(Users.name,session.query(UserType.catagory).filter(Users.user_type_id==UserType.id).as_scalar()).all()
# print(result)

# q1 = session.query(Users).filter(Users.id>2).subquery()
# res = session.query(q1).all()
# print(res)
#
# session.commit()
# session.close()


# import time
# from concurrent.futures import ThreadPoolExecutor
#
#
# def func(n):
#     time.sleep(1)
#     # print(n)
#     return n * n
#
#
# def call_back(m):
#     print('result:%s' % m.result())
#
#
# # 定义一个线程池对象，指定同时可以运行的最大线程数
# tpool = ThreadPoolExecutor(5)
# for i in range(20):
#     # 在线程池中调用回调函数
#     tpool.submit(func, i).add_done_callback(call_back)
#
# # tpool.map(func,range(10))
#
# t_lst = []
# for i in range(30):
#     t = tpool.submit(func, i)
#     t_lst.append(t)
#
# # 等待线程池中的所有子线程执行完毕，才执行主进程后面的代码
# tpool.shutdown()  # close+join
#
# # 获取自进程的返回值
# for res in t_lst:
#     print(res.result())
#
# print('主线程')

# f = lambda x,y:x if x>y else y
# print(f(10,9))

# li = [[1,2,3,4],[11,22,33,44]]
# fi_li = [i for j in li for i in j]
# print(fi_li)

# li = [11,3,2,11,3,56,2,1,4,8,7,5,2]
#
# ne_li = []
# for i in li:
#     if i not in ne_li:
#         ne_li.append(i)
#
# print(ne_li)

# print("%s"*3)
# print(["%s"]*3)
# print(["%s" for i in range(3)])
# print((1,2,3)*2)


# # 将多维数组展开为一维数组
# def odf(li):
#     res_li = []
#     for i in li:
#         if isinstance(i,list):
#             for j in odf(i):
#                 res_li.append(j)
#         else:
#             res_li.append(i)
#     return res_li
#
# test_li = [1,2,3,[15,234,[234,67,22,[423,65,23,76]]]]
# print(odf(test_li))


# import pymongo
#
# client = pymongo.MongoClient(host='10.1.1.128',port=27017)
# db = client.test
# my_coll = db.students
#
# stu1 = {
#     'name':'zx',
#     'age':32,
#     'gender':'male'
# }
#
# # res = my_coll.insert(stu1)
# # print(res)
#
# res = my_coll.find({'age':{'$gt':20}})
# for i in res:
#     print(i.get('name'))

# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com/')
# print(browser.page_source)
# browser.close()

# from selenium import webdriver
#
# browser = webdriver.Chrome()
#
# browser.get("https://www.taobao.com")
# li = browser.find_elements_by_css_selector('.service-bd li')
# for i in li:
#     print(i)
#
# browser.close()

# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome()
# browser.get("https://www.taobao.com")
# sear_inp = browser.find_element_by_id('q')
# sear_inp.send_keys('iphone')
# time.sleep(1)
# sear_inp.clear()
# sear_inp.send_keys('matchbox')
# button = browser.find_element_by_class_name('btn-search')
# button.click()

# li1 = [1,2,3,4]
# li1.append(6)
# print(li1)
#
# li2 = [1,2,3,4]
# li3 = [6]
# li = li2+li3
# print(li)
#
# li2.extend(li3)
# print(li2)

# import numpy as np
# import pandas as pd
#
# t1 = np.array([True,False,False,False])
#
# print(np.count_nonzero(t1))

# t1 = np.arange(12).reshape(3,4).astype("float")
# print(t1)
# t2 = t1[t1[:,-1]<=7,]
# print(t2)
# t3 = t1[t1<=7]
# print(t3)

# 生成序列，必须是一维的数据
# t = pd.Series(data=np.arange(12).astype("float"),index=[chr(i+65) for i in range(12)])
# print(t)
# print("="*30)
#
# data_li = [{'name':'zx','age':120,'phone':231241,'dep':'dev'},
#            {'name': 'hehe', 'age': 134, 'phone': 32434234},
#            {'name': 'haha', 'phone': 65354, 'dep': 'hr'},
#            {'name': 'honji', 'age': 43,  'dep': 'ops'},
#            {'name': 'zdx', 'age': 232, 'phone': 888888, 'dep': 'CEO'},]
#
# # 生成数据框架，本质是一个二位的数组，有行列索引
# t1 = pd.DataFrame(data_li)
# # print(t1)
#
# # 找到并去除数据框架中的nan类型的几种方式
# t1["age"].fillna(t1["age"].mean(),inplace=True)
# t1["dep"].fillna(value="intership",inplace=True)
# t1.drop(t1[t1["phone"].isna()].index,inplace=True)
# # t1.dropna(inplace=True)
# print(t1)
#
# # 对数据框架型数据进行分片的几种方式
# print("="*30)
# print(t1[1:]["age"])
# print("="*30)
# print(t1.iloc[:,-1])
# print("="*30)
# print(t1.loc[(t1["name"]=="zx")|(t1.loc[:,"age"]>140),"dep"])

# 生成可以用于索引的时间类型
# time_stamp = pd.date_range(start="2019-1",periods=10,freq="2M")
# print(time_stamp.strftime("%Y_%m"))
'''
Index(['2019_01', '2019_03', '2019_05', '2019_07', '2019_09', '2019_11',
       '2020_01', '2020_03', '2020_05', '2020_07'],
      dtype='object')
'''

# li = [1,2,3,4,5,6,7,8,9]
# print(len(li))

# import random
#
# print(random.choice([1,2,3]))
# print(random.choices([1,2,3,4],k=2))
# '''
# 1
# [1, 3]
# '''


# # 字典生成式练习
#
# cookies="anonymid=j3jxk555-nrn0wh; _r01_=1; _ga=GA1.2.1274811859.1497951251;
# _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; ln_uact=mr_mao_hacker@163.com;
# depovince=BJ; jebecookies=54f5d0fd-9299-4bb4-801c-eefa4fd3012b|||||;
# JSESSIONID=abcI6TfWH4N4t_aWJnvdw; ick_login=4be198ce-1f9c-4eab-971d-48abfda70a50;
# p=0cbee3304bce1ede82a56e901916d0949; first_login_flag=1;
# ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20171230/1635/main_JQzq_ae7b0000a8791986.jpg;
# t=79bdd322e760beae79c0b511b8c92a6b9; societyguester=79bdd322e760beae79c0b511b8c92a6b9;
# id=327550029; xnsid=2ac9a5d8; loginfrom=syshome; ch_id=10016; wp_fold=0"
#
# cookies_dict = {cookie.split('=')[0]:cookie.split('=')[1] for cookie in cookies.split('; ')}
# print(cookies_dict)

# import requests
#
# session = requests.session()
# post_url = "http://www.renren.com/PLogin.do"
# post_data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
# }
# #使用session发送post请求，cookie保存在其中
# session.post(post_url,data=post_data,headers=headers)
# #在使用session进行请求登陆之后才能访问的地址
# r = session.get("http://www.renren.com/327550029/profile",headers=headers)
# print(r.content.decode())


# 线程队列结合多线程,实现并发
# import threading
# from queue import Queue
# import time
#
# q1 = Queue()
# q2 = Queue()
#
# for i in range(101):
#     q1.put(i)
#
# def test_func1():
#     while True:
#         i = q1.get()
#         time.sleep(0.2)
#         print(i)
#         q2.put(i + 100)
#         q1.task_done()
#
# def test_func2():
#     while True:
#         i = q2.get()
#         time.sleep(0.5)
#         print(i)
#         q2.task_done()
#
# th_li = []
# th1 = threading.Thread(target=test_func1)
# th_li.append(th1)
# th2 = threading.Thread(target=test_func2)
# th_li.append(th2)
#
# for th in th_li:
#     th.setDaemon(True)
#     th.start()
#
# for q in [q1,q2]:
#     q.join()
#
# print("finished!")

# from sklearn.feature_extraction import DictVectorizer
# from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
# from sklearn.preprocessing import MinMaxScaler,StandardScaler,Imputer
#
# class WrapSklearn(object):
#
#     def __init__(self,skobjname):
#         self.dvecobj = DictVectorizer()
#         self.cvecobj = CountVectorizer()
#         self.tivecobj = TfidfVectorizer()
#         self.mmsobj = MinMaxScaler()
#         self.ssobj = StandardScaler()
#         self.impobj = Imputer()
#         self.skobjname = skobjname
#
#     def dispatch(self):
#         if hasattr(self,self.skobjname):
#             skobj = getattr(self,self.skobjname)
#             return skobj
#         else:
#             raise Exception("no such skobj")
#
#     def run_fit_transform(self,data):
#         skobj = self.dispatch()
#         res = skobj.fit_transform(data)
#         return res
#
# if __name__ == '__main__':
#     myskobj = WrapSklearn("mmsobj")
#     data = [[ 1., -1., 3.],
#             [ 2., 4., 2.],
#             [ 4., 6., -1.]]
#     res = myskobj.run_fit_transform(data)
#     print(res)


# df = pd.DataFrame(np.random.randn(12).reshape((3,4)),index=list('abc'),columns=list('wxyz'))
# # print(df)
# '''
#           w         x         y         z
# a  0.724344  0.830823  1.427218  1.722364
# b  1.068529 -2.961252  0.090240 -1.163440
# c  1.292776  1.222545  1.125099  1.183954
# '''
# df_zindex = df.set_index(['z',])
# # print(df_zindex)
# '''
#                   w         x         y
# z
#  0.894270 -0.073219  0.399783  1.421480
# -0.996631  2.071505  0.390362  0.293151
#  0.036583 -0.972639 -0.968258  0.450996
# '''
# df_reset = df_zindex.reset_index()
# # print(df_reset)
# '''
#           z         w         x         y
# 0 -0.501322 -1.960289 -0.671179  0.286556
# 1  1.753814  0.522932  1.485377  0.412265
# 2  1.331297 -0.170554 -0.282364 -1.193989
#
# '''


# from sklearn.datasets import load_iris
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.model_selection import train_test_split
# from  sklearn.preprocessing import StandardScaler
#
# def pre_iris():
#     data = load_iris()
#     # print(data.feature_names)
#     # print(data.target_names)
#     '''
#     ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
#     ['setosa' 'versicolor' 'virginica']
#     '''
#     x_train,x_test,y_train,y_test = train_test_split(data.data,data.target,test_size=0.2)
#     # print(x_train)
#     knn = KNeighborsClassifier(n_neighbors=5)
#
#     # 数据标准化
#     stobj = StandardScaler()
#     x_train = stobj.fit_transform(x_train)
#     x_test = stobj.transform(x_test)
#     # print(x_test)
#     '''
#     [[ 1.1105262   0.52211112  1.20390926  1.27317919]
#      [ 0.39148046 -1.06118613  1.14756405  0.36066168]
#      [ 0.15179855 -0.15644485  0.86583801  0.88210026]
#     ... ...
#     '''
#
#     # 训练模型
#     knn.fit(x_train,y_train)
#
#     # 预测值
#     pre_res = knn.predict(x_test)
#     # print(pre_res)
#     '''
#     [2 1 2 0 2 1 0 2 1 2 1 1 2 0 2 1 2 2 0 2 2 0 1 0 0 2 1 0 0 1]
#     '''
#
#     # 计算预测准确率
#     accuracy = knn.score(x_test,y_test)
#     print(accuracy)
#     '''
#     1.0
#     '''
#
# if __name__ == '__main__':
#     pre_iris()


# import tensorflow as tf
#
# g = tf.get_default_graph()
# print(g)
#
# new_graph = tf.Graph()
# print(new_graph)
#
# a = tf.constant(1.0)
# b = tf.placeholder(tf.float32)
#
# sum = tf.add(a,b)
#
# print(a.graph)
#
# with tf.Session() as sess:
#     print(sess.run(sum,feed_dict={b:3.3}))


# import tensorflow as tf
#
# # 生成符合正太分别的随机tensor
# a = tf.random_normal([3,4],mean=0,stddev=1.0)
# a1 = tf.random_normal([2,4],mean=0,stddev=1.0)
# # 修改tensor的形状，生成新tendor
# b = tf.reshape(a,[2,6])
#
# print(a.shape)
# print(b.shape)
#
# # 转换tensor内的数据的类型为指定类型
# c = tf.cast(a,dtype=tf.int64)
#
# d = tf.placeholder(dtype=tf.float32,shape=[None,4])
# print(d)
# d.set_shape([3,4])
# print(d.get_shape())
#
# # 按行或者列合并两个tensor，按行合并，列数必须相同，按列合并，行数必须相同
# e = tf.cast(tf.concat([a,a1],axis=0),dtype=tf.float32)
# # e1 = tf.concat([a,a1],axis=1)
# f = tf.constant(-1,dtype=tf.float32,shape=[2,3])
#
# x = tf.constant([[4,6]])
# y = tf.constant([[2],[4]])
# z = tf.matmul(x,y)
#
# with tf.Session() as sess:
#     print(sess.run(a))
#     print(sess.run(b))
#     print(sess.run(c))
#     print(sess.run(d,feed_dict={d:[[1,2,3,4],[5,6,7,8],[9,10,11,12]]}))
#     print(sess.run(e))
#     # print(sess.run(e1))
#     print(sess.run(f))
#     print(sess.run(z))

# for i in [b"NZPP"][0].decode('utf-8'):
#     print(i)

# import threading
# import time
#
# i = 0
#
# def test_multhread():
#     global i
#     i += 1
#     time.sleep(2)
#     print(i)
#
# for i in range(10):
#     t = threading.Thread(target=test_multhread)
#     t.start()

# import threading
# import time
#
# try:
#     import greenlet
#     get_tid = greenlet.getcurrent
# except Exception as e:
#     get_tid = threading.get_ident
#
#
# class Local(object):
#
#     DICT = {}
#
#     def __getattr__(self, item):
#         tid = get_tid()
#         if tid in self.DICT:
#             return self.DICT[tid].get(item)
#         return None
#
#     def __setattr__(self, key, value):
#         tid = get_tid()
#         if tid in self.DICT:
#             self.DICT[tid][key] = value
#         else:
#             self.DICT[tid] = {key:value}
#         return None
#
# obj = Local()
#
# def test_local(i):
#     obj.record = i
#     time.sleep(2)
#     print(obj.record)
#
# def get_threads(n):
#     for i in range(n):
#         t = threading.Thread(target=test_local,args=[i,])
#         t.start()
#     return None
#
# get_threads(10)

# a = np.arange(1,100,2).reshape(10,5)
# print(a)
# print(a.ndim) # 输出数组的维度
# print(a.size) # 输出总共有几个元素
# print(a.shape)

# a = np.random.randint(1,50,size=(3,4))
# # print(a)
#
# b = np.random.randint(1,50,size=(2,4))
# # print(b)
#
# c = np.concatenate((a,b),axis=0)
# print(c)
#
# # print(np.split(c,[1,4],axis=0)) # 注意：切割数组中明确的范围是左闭右开区间
# '''
# [array([[15, 32, 38, 46]]), array([[ 6,  8,  5, 26],
#        [20, 48, 37, 12],
#        [25, 36, 33, 40]]), array([[ 1, 44, 45, 35]])]
# '''
# print(c.sum(axis=1))
# print(c.mean(axis=0))
#
# c.sort(axis=1) # 改变自身的排序
# print(c)
# print(np.sort(c,axis=0)) # 不改变自身，返回排序后的新变量
#
# print(np.partition(c,kth=3,axis=0))
#
# print(np.random.randint(1,10))

# from matplotlib import pyplot as plt
#
# pic = np.random.randint(0,255,size=(200,1,3))
#
# a_li = [1,2,3]
# print(a_li*3)

# col = pd.MultiIndex.from_product([['qizhong','qimo'],
#                                 ['chinese','math']])
#
# ind = pd.MultiIndex.from_product([['class4'],['zhangsan','lisi']])
#
# df = pd.DataFrame(data=np.random.randint(60,120,size=(2,4)),index=ind,columns=col)
#
# print(df)
#
# # df.loc['class4','lisi']['qizhong','math'] = np.nan
# print(df.qizhong.math['class4']['lisi'])
# print(df.qizhong.math['class4','lisi'])
#
# print(df)

# import pyaml
#
# def build_yaml_file(raw_data,file_name):
#     try:
#         res_yml = pyaml.dumps(raw_data).decode('utf-8')
#         with open(file_name,'w',encoding='utf-8') as f:
#             for line in res_yml:
#                 f.write(line)
#         return True
#     except Exception as e:
#         print(str(e))
#         return False
#
# data = [{'hosts': 'sample_group_name', 'tasks': [{'name': 'just an uname', 'command': 'uname -a'}]}]
# res = build_yaml_file(data,'test.yml')
#
# if res:
#     print('test.yml created successfully!')

# data = [{'hosts': 'sample_group_name', 'tasks': [{'name': 'just an uname', 'command': 'uname -a'}]}]
# res_yml = pyaml.dumps(data)
#
# print(res_yml.decode('utf-8'))
# '''
# - hosts: sample_group_name
#   tasks:
#     - command: 'uname -a'
#       name: 'just an uname'
# '''

# 在python中使用抽象类
# import abc
#
# class MyBase(metaclass=abc.ABCMeta):
#
#     # 被这个装饰器装饰过的函数，
#     # 必须要被其子类实现，
#     # 否则子类实例化时报错
#     @abc.abstractmethod
#     def send(self):
#         pass
#
#     @abc.abstractmethod
#     def recv(self):
#         pass
#
# class Foo(MyBase):
#
#     def foofunc(self):
#         print('a test')
#
#     def send(self):
#         print('in send')
#
#     def recv(self):
#         print('in recv')
#
# foo = Foo()
# foo.send()

# class MyBase(object):
#
#     def send(self):
#         raise NotImplementedError('必须实现send方法')
#
# class Foo(MyBase):
#
#     pass
#
# foo = Foo()
# foo.send()

# from bs4 import BeautifulSoup

xml_text = '''
"<error>
<ret>0</ret>
<message></message>
<skey>@crypt_ac8812af_0ffde1190007c7c044bc31ae51407c45</skey>
<wxsid>fRwfacRtjRFpEIwt</wxsid>
<wxuin>1062220661</wxuin>
<pass_ticket>0M1plebTzNQ%2FKaSIfTfk65laCSXUWmjpxvJEerZSnBaEDjNIyOafaQLtpQBhnCDa</pass_ticket>
<isgrayscale>1</isgrayscale></error>"
'''

# def build_xml_dict(xmltxt):
#     xml_dict = {}
#
#     soup = BeautifulSoup(xmltxt,'html.parser')
      # 找到一个标签内部的所有标签，但是不包括标签本身
#     tags = soup.find(name='error').find_all()
#     for tag in  tags:
#         xml_dict[tag.name] = tag.text
#     return xml_dict
#
# info_dict = build_xml_dict(xml_text)
# print(info_dict)

# def build_xml_dict(xmltxt):
#     xml_dict = {}
#
#     soup = BeautifulSoup(xmltxt,'html.parser')
#     tags = soup.find_all()
#     for tag in  tags:
#         xml_dict[tag.name] = tag.text
#     return xml_dict
#
# info_dict = build_xml_dict(xml_text)
# print(info_dict)

# from urllib import parse
#
# url = "/cgi-bin/mmwebwx-bin/webwxgeticon?" \
#       "seq=620250015&" \
#       "username=@a35dff2d43b56c53bb7cdb5a3887f35d&" \
#       "skey=@crypt_ac8812af_5a0f13bccf3adfcf32a33908924188de"
# v = parse.urlencode({'k1':url})
#
# tt = '''
# k1=%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxgeticon
# %3Fseq%3D620250015%26username%3D%40a35dff2d43b56c53bb7cdb5a3887f35d%26
# skey%3D%40crypt_ac8812af_5a0f13bccf3adfcf32a33908924188de
# '''
# print(v)

# print(parse.urlparse(url).query)

# import keyword
#
# print(keyword.kwlist)
#
# res = keyword.iskeyword('is')
# print(res)

# import json

# test_li = [
#     {'name':'zx','age':100},
#     {'name':'hj','age':300},
#     {'name':'zf','age':200},
# ]
#
# with open('jsontest.txt','w',encoding='utf-8') as f:
#     f.write(json.dumps(test_li))

# with open('jsontest.txt','r',encoding='utf-8') as f:
#     # for line in f:
#     #     print(line)
#     res = f.read()
#
# print(json.loads(res)[0]['name'])


# def get_sum(num):
#     if num == 1:
#         return 1
#     tmp = get_sum(num-1)
#     return num + tmp
#
# print(get_sum(3))


# class TestCa(object):
#
#     count = 0
#
#     def __init__(self,name):
#         self.name = name
#         TestCa.count += 1
#
#     def __str__(self):
#         return "%s是第%s个工具"%(self.name,self.count)
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
# print(TestCa("dajiba"))
# print(TestCa("damimi"))
# print(TestCa("dapipi"))
#
# print(TestCa.get_count())
# print(TestCa("dabibi").get_count())


# class SingleInstance(object):
#
#     instance = None
#     initflag = False
#
#     def __new__(cls, *args, **kwargs):
#         if cls.instance is None:
#             print('new function')
#             cls.instance = super().__new__(cls)
#             return cls.instance
#         return cls.instance
#
#     def __init__(self,name,age):
#         if not SingleInstance.initflag:
#             print('init function')
#             self.name = name
#             self.age = age
#             SingleInstance.initflag = True
#         else:
#             return
#
# a = SingleInstance('zx',100)
# b = SingleInstance('hj',22)
#
# print(id(a),a.name)
# print(id(b),b.name)


# class MyException(BaseException):
#
#     def __init__(self,msg):
#         self.msg = msg
#
# try:
#     raise MyException('test myexception')
# except MyException as e:
#     print(e)

# try:
#     raise Exception('test myexception')
# except Exception as e:
#     print(e)

# import random
#
# print(random.__file__)
# print(__file__)

# from test_import.myreceive import test_rec
# from test_import.mysend import test_send
#
# test_rec()
# test_send()
#
# import test_import
#
# test_import.mysend.test_send()

# import importlib
#
# func_name = "test_import.myreceive.test_rec"
# module_name,fin_name = func_name.rsplit(".",1)
#
# my_modeule = importlib.import_module(module_name)
# myfunc = getattr(my_modeule,fin_name)
#
# myfunc()

# mydict = "{'name':'zx','age':100}"
# mylist = "[{'name':'zx','age':100},{'name':'hj','age':101}]"
# mycal = "(3+4)*2"
# myfunc = "lambda :print('lambda function')"
#
# li = [mydict,mylist,mycal,myfunc]
#
# for i in li:
#     print(type(i),type(eval(i)))
#     res = eval(i)
#     print(res)
#     if callable(res):
#         res()

# 不建议使用eval函数直接解析用户输入的信息
# content = input("please input the calculation: ") # __import__('os').system('dir')
# res = eval(content.strip())
# print(res)

# import random
#
# print(random.randint(0,2))

# class A(object):
#     school = "BJU"
#
#     def __init__(self,name):
#         self.name = name
#
#     def show_name(self):
#         print(self.name)
#
#     @staticmethod
#     def show_info():
#         print('this is a test class')
#
#     @classmethod
#     def show_school(cls):
#         print(cls.school)
#
#     @property
#     def myname(self):
#         print('my property')
#         return self.name
#
# a =A('zx')
# a.show_name()
# a.show_info()
# a.show_school()
# print(a.myname)

# class A(object):
#     def __init__(self,myprice):
#         self.__price = myprice
#
#     @property
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self,val):
#         self.__price = val
#
#     @price.deleter
#     def price(self):
#         del self.__price
#
# a = A(100)
# print(a.price)
# a.price = 200
# print(a.price)
# del a.price
# # print(a.price)
#
# class B(object):
#     def __init__(self,myprice):
#         self.__price = myprice
#
#     def get_price(self):
#         return self.__price
#
#     def set_price(self,val):
#         self.__price = val
#
#     def del_price(self):
#         del self.__price
#
#     PRICE = property(get_price,set_price,del_price)
#
# b = B(10)
# print(b.PRICE)
# b.PRICE = 20
# print(b.PRICE)
# del b.PRICE
# # print(b.PRICE)

# def myfib1(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     a,b = 0,1
#     for i in range(n-1):
#         a,b = b,a+b # a=1,b=1 a=1,b=2
#     return a
#
# def myfib2(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return myfib2(n-2)+myfib2(n-1)
#
# for i in range(1,10):
#     # res = myfib1(i)
#     res = myfib2(i)
#     print(res,end=' ')

# import struct
#
# def pack_num(num):
#     '''
#     把数字格式化为用四个字节表示的的二进制数
#     :param num:
#     :return:
#     '''
#     if num.isdigit():
#         num = int(num.strip())
#     if not isinstance(num,int):
#         return False
#     str_num = struct.pack("i",num)
#     return str_num
#
# def unpack_num(bnum):
#     '''
#     把四个字节的二进制数，重新转换为十进制数字
#     :param bnum:
#     :return:
#     '''
#     if not isinstance(bnum,bytes):
#         return False
#     num = struct.unpack("i",bnum)[0]
#     return num
#
# print(pack_num("1"))
# # b'\x01\x00\x00\x00'
#
# res = pack_num("1001")
# print(unpack_num(res))
# # 1001

# name = b'ask;lask;ask'
# print(name)
# del name
# print(name) # NameError: name 'name' is not defined

# def write_file(filename,content):
#     with open(filename,'ab') as f:
#         f.write(content)
#
# def read_file(filename):
#     with open(filename,'rb') as f:
#         content = f.read()
#     return content
#
# recved_data = b''
# total_rec_len = 0
# total_len = 10000
# limit_len = 100
#
# while True:
#     recved_data += b'this '
#     rec_len = len(recved_data)
#
#     if rec_len == limit_len:
#         write_file('my_test_file', recved_data)
#         total_rec_len += limit_len
#         recved_data = b''
#         rec_len = 0
#
#     if total_rec_len >= total_len:
#         break
#
# print(len(read_file('my_test_file')))

# import os
# # 查看某个模块，在文件系统中的绝对路径
# print(os.__file__)

# import gevent
# from gevent import monkey
# import requests
#
# monkey.patch_all()
#
# def get_page_content(dst_url):
#     res = requests.get(url=dst_url)
#     print(len(res.text))
#
# url_li = [
#     "https://stackoverflow.com/",
#     "https://www.baidu.com/",
#     "https://www.microsoft.com/zh-cn/",
#     "https://www.apple.com/",
#     "https://tensorflow.google.cn/",
# ]
#
# spawn_li = []
# for url in url_li:
#     spawn_li.append(gevent.spawn(get_page_content,url))
#
# gevent.joinall(spawn_li)

# import time
# from concurrent.futures import ThreadPoolExecutor
#
# def func(n):
#     time.sleep(1)
#     # print(n)
#     return n * n,n + n
#
# def call_back(m):
#     # print('result:%s' % m.result())
#     print(m.result())
#
# # # 定义一个线程池对象，指定同时可以运行的最大线程数
# tpool = ThreadPoolExecutor(5)
# # for i in range(20):
# #     # 在线程池中调用回调函数
# #     tpool.submit(func, i).add_done_callback(call_back)
#
# # tpool.map(func,range(10))
#
# t_lst = []
# for i in range(30):
#     t = tpool.submit(func, i)
#     t_lst.append(t)
# #
# # # 等待线程池中的所有子线程执行完毕，才执行主进程后面的代码
# tpool.shutdown()  # close+join
# #
# # # 获取自进程的返回值
# for res in t_lst:
#     print(res.result())
#
# print('主线程')

# import gevent
# from gevent import monkey
# import requests
#
# monkey.patch_all()
#
# def get_page_content(dst_url):
#     res = requests.get(url=dst_url)
#     return dst_url,len(res.text)
#
# url_li = [
#     "https://stackoverflow.com/",
#     "https://www.baidu.com/",
#     "https://www.microsoft.com/zh-cn/",
#     "https://www.apple.com/",
#     "https://tensorflow.google.cn/",
# ]
#
# spawn_li = []
# for url in url_li:
#     spawn_li.append(gevent.spawn(get_page_content,url))
#
# gevent.joinall(spawn_li)
#
# for g in spawn_li:
#     print("from %s received %d byte data."%(g.value[0],g.value[1]))

# from multiprocessing import Pool
# import time
#
# def foo(i):
#     time.sleep(0.5)
#     return i
#
# def bar(arg):
#     # 回调函数，每个子进程运行结束后，主进程调用此函数，arg是foo函数的返回值
#     print("callback function")
#     print('hello %s'%arg)
#
# pool = Pool(5) # 每次五个线程一起运行，运行完再进来五个一起运行
# for i in range(20):
#     pool.apply_async(func=foo,args=(i,),callback=bar)
#
# # 这两个必须按这个顺序写
# pool.close()
# pool.join()
#
# print('end of main process')

# def myfib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     a,b = 0,1
#     for i in range(n-1):
#         a,b = b,a+b
#     return a
#
# def myfib2(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     res = myfib2(n-2)+myfib(n-1)
#     return res
#
# for i in range(1,100):
#     res = myfib2(i)
#     print(res)

# final_level_leaves = 21
# middle_num = divmod(final_level_leaves,2)[0]
# # print(middle_num)
#
# for i in range(1,final_level_leaves+1,2):
#     # blanknum = divmod(final_level_leaves-i,2)[0]
#     blanknum = int((final_level_leaves-i)/2)
#     print(" "*blanknum,end='')
#     print("^"*i)
#
# for j in range(5):
#     print(" " * middle_num, end='')
#     print("|")

# dict_li = [
#     {'name':'zx','age':120},
#     {'name':'xr','age':100},
#     {'name':'hj','age':110},
#     {'name':'hh','age':20},
#     {'name':'xn','age':19},
# ]
# res = sorted(dict_li,key=lambda mydict:mydict['age'],reverse=True)
# print(res)

# li = ['zx','hj','xr']
# print(','.join(li))
#
# li2 = ['''"zx"''','''"hj"''','''"xr"''']
# print(','.join(li2))

# import re
#
# res = re.split(r':| ','names:zx ds as wq')
# print(res)

# my_dict = {}
# my_dict['count'] = 0
# my_dict['count'] += 1
# print(my_dict)

# level1_key_li = ['a','b','c']
# level2_key_li = [1,2,3,3]
# my_dict = {}

# for k1 in level1_key_li:
#     if k1 not in my_dict:
#         # my_dict.setdefault(k1,{})
#         my_dict[k1] = {}
#     for k2 in level2_key_li:
#         if k2 not in my_dict[k1]:
#             my_dict[k1][k2] = 1
#         else:
#             my_dict[k1][k2] += 1
#
# print(my_dict)

# for k1 in level1_key_li:
#     for k2 in level2_key_li:
#         my_dict.setdefault(k1,{})
#         my_dict[k1].setdefault(k2,0)
#         my_dict[k1][k2] += 1
#
# print(my_dict)
#

# f = open('temp.txt','r')
# while True:
#     res = f.read(10)
#     if not res:
#         break
#     print(res,end=' ')
# f.close()
#
# while True:
#     res = f.readline()
#     if not res:
#         break
#     print(res,end='')
# f.close()
#
# res = f.readline()
# print(res)
# # f.close()
#
# res_li = f.readlines()
# f.close()
# print(res_li)

# def juge_num(num):
#     for i in range(2,num//2+1):
#         if num % i == 0:
#             return False
#     else:
#         return True
#
# def sushu(num):
#     tmp = []
#     if juge_num(num):
#         return [1, num]
#
#     while True:
#         if juge_num(num) and num != 1:
#             tmp.append(num)
#             break
#         else:
#             for i in range(2, num//2+1):
#                 if num % i == 0 & juge_num(i):
#                     tmp.append(i)
#                     num = num//i
#                     break
#     return tmp
#
# print(sushu(36))

# import socket
#
# hostip = socket.gethostbyname('www.taobao.com')
# print(hostip)
# conn = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
# conn.settimeout(10)
# conn.connect((hostip,80))
# conn.send('GET / HTTP/1.1\r\n'.encode('utf-8'))
# res = conn.recv(1024)
# print(res.decode('utf-8'))

# import nmap
# import socket
#
# def mynmapscan(tgip,tgports):
#     nmobj = nmap.PortScanner(nmap_search_path=('nmap',r"D:\Program Files (x86)\Nmap\nmap.exe"))
#     nmobj.scan(tgip,tgports)
#     for tgport in tgports.split(','):
#         state = nmobj[tgip]['tcp'][int(tgport)]['state']
#         print(state)
#
# mynmapscan(socket.gethostbyname('www.taobao.com'),'22,53,110,143')
# mynmapscan(socket.gethostbyname('www.taobao.com'),'22')

# print(2**15)

# import nmap
#
# def find_tags(host_addrs):
#     nmobj = nmap.PortScanner(nmap_search_path=('nmap', r"D:\Program Files (x86)\Nmap\nmap.exe"))
#     nmobj.scan(host_addrs, '445')
#
#     tag_host_li = []
#     # print(nmobj.all_hosts()) # 找到所有在线主机
#     for hostaddr in nmobj.all_hosts():
#         if nmobj[hostaddr].has_tcp(445): # 查看在线主机是否运行了445端口
#             state = nmobj[hostaddr]['tcp'][445]['state'] #获取端口状态
#             if state == 'open':
#                 print('[-] find %s opened 445 port'%hostaddr)
#                 tag_host_li.append(hostaddr)
#     return tag_host_li
#
# res = find_tags('192.168.31.1-254')
# print(res)

# test_str = '\x00\x11\x50\x24\x68\x7F\x00\x00'
# raw_test_str = 'r"%s"' % test_str

# def val2addr(addr_x):
#     addr = ''
#     for ch in addr_x:
#         addr += ("%02x "%ord(ch))
#     addr = addr.strip().replace(' ',':')[0:-6]
#     print(addr)
#     return addr

# import re
#
# res_li = re.findall(r'\\x(\w{2})',test_str)
# print(res_li)
# mac_addr = ':'.join(res_li[0:-2])
# print(mac_addr,type(mac_addr))

# from winreg import *
#
# net = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
# key = OpenKey(HKEY_LOCAL_MACHINE,net)
#
# def val2addr(addr_x):
#     addr = ''
#     for ch in addr_x:
#         addr += ("%02x "%ord(ch))
#     addr = addr.strip().replace(' ',':')[0:-6]
#     print(addr)
#     return addr
#
#
# for i in range(100):
#     try:
#         guid = EnumKey(key,i)
#         netkey = OpenKey(key,str(guid))
#         n,addr,t = EnumValue(netkey,5)
#         n,netname,t = EnumValue(netkey,4)
#         mac_addr = val2addr(addr)
#         netname = str(netname)
#
#         print('[+] %s : %s'%(netname,mac_addr))
#         CloseKey(netkey)
#     except Exception as e:
#         break

# import os
#
# def check_recycler():
#     recycle_path_li = ['C:\\Recycled\\','C:\\$Recycle.Bin\\']
#     for recycle_dir in recycle_path_li:
#         if os.path.isdir(recycle_dir):
#             return recycle_dir
#     return None
#
# res = check_recycler()
# print(res)
#
# sids_li = os.listdir(res)
# for sid in sids_li:
#     del_files = os.listdir(os.path.join(res,sid))
#     print(del_files)

# def get_closed_num(num):
#     mnum = num - int(num)
#     if mnum >= 0.5:
#         num = int(num) + 1
#     else:
#         num = int(num)
#     return num
#
# print(get_closed_num(12.3))
# print(get_closed_num(12.6))

# import easygui
#
# easygui.msgbox('dianwo')

# from queue import LifoQueue
#
# test_str = '(((((((((()()(()))))))'
# mystack = LifoQueue()
#
# # mystack.put(1)
# # mystack.put(3)
# # mystack.put(23)
# # print(mystack.get())
#
# flag = True
# for i in test_str:
#     if i == '(':
#         mystack.put(i)
#     else:
#         if i == ')':
#             try:
#                 mystack.get_nowait()
#             except:
#                 flag = False
#                 print('cannot find a match for (')
#
# if mystack.qsize() > 0 or not flag:
#     print('not a valid calculation')
# else:
#     print('all matched')

# for i in range(10,-1,-2):
#     print(i)

# import time
# final_num = int(input('how many seconds: ').strip())
# for i in range(final_num,0,-1):
#     print('\r',i,end='',flush=True)
#     time.sleep(1)
# print('\nblast off')

# final_num = int(input('how many seconds: ').strip())
# for i in range(final_num,0,-1):
#     print('\r',i,"* "*i,end='',flush=True)
#     # print("*"*i)
#     time.sleep(1)
# print('\nblast off')

# li = ['zx','hj','lx','xr','cx']
# li.remove(li[1])
# print(li)
# li.insert(1,'xy')
# print(li)

# li = [1,1,3,2,1,4,8,1,4,5,8,6,2,1,4,7,2,7,9,1,3,8,6,5]

# for i,v in enumerate(li):
#     j = i+1
#     while j < len(li):
#         if li[i] == li[j]:
#             del li[j]
#             continue
#         j += 1
# print(li)

# for i,v in enumerate(li):
#     for j, k in enumerate(li,start=i+1):
#         try:
#             if li[i] == li[j]:
#                 del li[j]
#         except:
#             break
# print(sorted(li))

# for i in range(len(li)):
#     for j in range(i+1,len(li)):
#         try:
#             if li[i] == li[j]:
#                 del li[j]
#         except:
#             break
# print(sorted(li))

# for i in range(len(li)):
#     j = i+1
#     print(li)
#     while j < len(li):
#         if li[i] == li[j]:
#             del li[j]
#             continue
#         j += 1
# print(li)

# import copy
#
# def add_ele_new(ori_li):
#     new_li = copy.copy(ori_li)
#     new_li.append('newli')
#     return new_li
#
# def add_ele(ori_li):
#     new_li = ori_li
#     new_li.append('newli')
#     return new_li
#
# li = [1,2,3,4]
#
# res = add_ele(li)
# print(li)
# print(res)

# def get_total_yuan(fen,jiao,yuan):
#     fen_yuan = fen//100
#     fen_jiao = fen%100//10
#     ffen = fen%100%10
#
#     jiao_yuan = jiao//10
#     fjiao = jiao%10
#
#     total_yuan = yuan + jiao_yuan +fen_yuan + (fen_jiao+fjiao)*0.1 + ffen*0.01
#     return total_yuan
#
# fen = 12
# jiao = 24
# yuan = 1
#
# print(get_total_yuan(fen,jiao,yuan))

# import random
# import time
#
# res = random.choices(range(1,21),k=5)
# print(res)
#
# for i in range(10):
#     my_fnum = "%.02f"%random.random()
#     print(my_fnum)
#     time.sleep(3)

# from pygame.color import THECOLORS
# import random
#
# res = THECOLORS.keys()
# print(list(res))

# size = width,height = 60,100
# print(size)

# import requests
#
# res = requests.get('http://www.baidu.com')
# print(res.content.decode('utf-8'))

# import pygame
# # 获取以及被使用的事件编号个数
# print(pygame.USEREVENT) # 24
# # 获取最多可以定义多少个事件
# print(pygame.NUMEVENTS) # 32

# print("test %.02f"%112.12)

# import pickle
#
# data = {'name':'zx','gender':'male'}
# f = open('temp','wb')
# pickle.dump(data,f)
# f.close()
