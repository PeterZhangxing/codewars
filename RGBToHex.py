#!/usr/bin/python3.5

def check_num(i):
    if i < 0:
        i = 0
    elif i > 255:
        i = 255
    return i

def rgb(r, g, b):
    r = check_num(r)
    g = check_num(g)
    b = check_num(b)

    hl = []
    rh = hl.append(hex(r).split('x')[1].upper())
    gh = hl.append(hex(g).split('x')[1].upper())
    bh = hl.append(hex(b).split('x')[1].upper())

    hl2 = []
    for item in hl:
        if len(item) < 2:
            item = "0" + item
        hl2.append(item)

    res = "".join(hl2)
    return res


if __name__ == "__main__":
    print(rgb(2545,23,55))