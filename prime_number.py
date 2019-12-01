#!/usr/bin/python3.5

def isPrime(n):
    if n <= 1:
      return False
    i = 2
    while i*i <= n:
      if n % i == 0:
        return False
      i += 1
    return True

def gap(g, m, n):
    gap_li = []
    first_p = 0
    sec_p = 0

    for i in range(m,n+1):
        if isPrime(i) and first_p == 0:
            first_p = i
        elif isPrime(i) and first_p != 0:
            sec_p = i
            if sec_p - first_p == g:
                gap_li.extend([first_p,sec_p])
                return gap_li
            else:
                first_p = sec_p
    if first_p == sec_p or first_p == 0 or sec_p == 0:
        return None


if __name__ == "__main__":
    print(gap(2,100,110))
    print(gap(4,100,110))
    print(gap(6,100,110))
    print(gap(8,300,400))
    print(gap(10,300,400))