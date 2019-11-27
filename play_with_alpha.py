#!/usr/bin/python3.5

def accm(arg):
    li = list(arg)
    res_li = []
    for i,v in enumerate(li):
        temp = v.upper() + v.lower() * i
        res_li.append(temp)
    res = "-".join(res_li)
    return res


if __name__ == '__main__':
    res = accm("aBcdF")
    print(res) # A-Bb-Ccc-Dddd-Fffff