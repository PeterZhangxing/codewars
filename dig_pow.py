#!/usr/bin/python3.5

def dig_pow(n, p):
    sn = str(n)
    iter_n = sum(int(v)**(i+p) for i,v in enumerate(sn))
    if str(iter_n/n).split('.')[1] == '0':
        return int(iter_n/n)
    else:
        return -1

if __name__ == "__main__":
    print(dig_pow(89, 1))
    print(dig_pow(46288, 3))
    print(dig_pow(92, 1))