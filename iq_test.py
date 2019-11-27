#!/usr/bin/python3.5

def iq_test(numbers):
    nlist = numbers.split()

    c_odd = 0
    c_even = 0
    for i,v in enumerate(nlist):
        if int(v) == 1 or int(v) % 2 != 0:
            c_odd += 1
        else:
            c_even += 1

    if c_odd == 1:
        for i,v in enumerate(nlist):
            if int(v) == 1 or int(v) % 2 != 0:
                return i+1
    else:
        for i,v in enumerate(nlist):
            if int(v) % 2 == 0:
                return i+1


if __name__ == "__main__":
    print(iq_test("2 4 7 8 10"))
    print(iq_test("1 2 2"))