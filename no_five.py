#!/usr/bin/python3.5

def dont_give_me_five(start,end):
    n = 0
    for i in range(start,end+1):
        if '5' not in list(str(i)):
            n += 1
    return n

if __name__ == "__main__":
    n = dont_give_me_five(4,17)
    print(n)