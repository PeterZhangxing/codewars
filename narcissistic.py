#!/usr/bin/python3.5

def narcissistic(value):
    sv = str(value)
    vl = len(sv)
    sl = []

    for s in sv:
        sl.append(int(s)**vl)
    if sum(sl) == value:
        return True
    else:
        return False


if __name__ == "__main__":
    print(narcissistic(7))
    print(narcissistic(4887))
    print(narcissistic(371))