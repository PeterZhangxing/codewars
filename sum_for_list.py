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

def primeList(num):
    num = abs(num)
    li = set()
    for i in range(2,num+1):
        if num % i == 0 and isPrime(i):
            li.add(i)
    return li

def sum_for_list(lst):
    fin_set = set()
    for l_mem in lst:
        fin_set.update(primeList(l_mem))
    fin_list = sorted(list(fin_set))

    sum_list = []
    tmp_list = []
    for i in fin_list:
        tmp_list.append(i)
        count = 0
        for v in lst:
            if v % i == 0:
                 count += v
        tmp_list.append(count)
        sum_list.append(tmp_list)
        tmp_list = []

    return sum_list


if __name__ == "__main__":
    print(sum_for_list([-12,-15]))
    print(sum_for_list([10,12,15,21,35]))