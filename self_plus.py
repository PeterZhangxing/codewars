#!/usr/bin/python3.5

def digital_cal(n):
    nst = str(n)
    sni = 0
    for i in nst:
        sni = sni + int(i)
    return sni

def digital_root(n):
    tnum = n
    while tnum > 9:
        tnum = digital_cal(tnum)
    return tnum

if __name__ == "__main__":
    num_sum = digital_root(123924765757767665)
    print(num_sum)
