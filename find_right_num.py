#/usr/bin/python3.5

import math

for i in range(1,1000):
    x = i + 268
    y = i + 100

    sqrt_x = int(math.sqrt(x))
    sqrt_y = int(math.sqrt(y))

    if  sqrt_x**2 == x and sqrt_y**2 == y:
        print(i)

        