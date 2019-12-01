#!/usr/bin/python3.5

def countBits(n):
    bsl = list(bin(n).split('b')[1])
    count = 0
    for i in bsl:
        if i == '1':
            count += 1
    return count

if __name__ == "__main__":
    print(countBits(1234))