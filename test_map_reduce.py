#!/usr/bin/python3.5

from functools import reduce

li = [1,2,3,4,5,6,7,8,9]

resm = map(lambda x:x*x,li)
# 对可迭代对象中的每个值，执行前面定义的函数，返回的是一个执行函数后生成的可迭代对象
resm_li = list(resm)
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

resf = filter(lambda x:x>2,li)
# 对可迭代对象中的数值都进行函数中定义的判断，返回的是符合判断的值组成的可迭代对象
resf_li = list(resf)
# [3, 4, 5, 6, 7, 8, 9]

resr1 = reduce(lambda x,y:x+y,li,5)
# 让可迭代对象中的每个值，都执行前面定义的函数，最后得到一个结果，第三个参数表示最后得出的结果，再按照前面的函数执行一次操作
# 50

print(resm_li)
print(resf_li)
print(resr1)