#!/usr/bin/python3.5

import math

def find_rightnum():
    res = []
    for i in range(1,10):
        for j in range(1,10):
            num = 1000*i + 100*i + 10*j + j
            if math.sqrt(num) == int(math.sqrt(num)):
                res.append(num)
    return res

if __name__ == "__main__":
    print(find_rightnum())
