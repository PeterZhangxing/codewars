#!/usr/bin/python3.5

def fib(num):
    '''
    用递归算法求一个数的阶乘
    :param num:
    :return:
    '''
    if num == 1:
        rec_mul = 1
    else:
        rec_mul = fib(num-1)*num
    return rec_mul


if __name__ == "__main__":
    while True:
        num = input("number you want to calculate the factorios :")
        if num == "exit" or num.upper() == "Q":
            exit("quit this programme")
        res = fib(int(num))
        print(res)