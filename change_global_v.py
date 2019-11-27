#!/usr/bin/python3.5

#### 设置变量为外层函数的变量，而不是本函数中新定义的局部变量 ####

def outer_func(param):
    b = param
    def inner_func():
        # 设置变量为该函数的外层的变量
        nonlocal b
        b += 1
    inner_func()
    print(b)

outer_func(10)

##### 全局变量的使用 #####

num = 100

def test_nolo():
    # 设置该变量为全局变量，而不是局部变量
    global num
    num += 1
    print(num)

test_nolo()