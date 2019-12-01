#!/usr/bin/python3.5

# def s_num(org,num):
#     n = org
#     while n*n <= num:
#         if n*n == num:
#             return True
#         n += 1
#     return False

def s_num(num):
    import math
    res = int(math.sqrt(num))
    return res*res == num

def list_squared(m, n):
    fin_list = []
    for i in range(m,n+1):
        tmp_list = []
        stmp = sum(x*x for x in range(1,i+1) if i % x == 0)
        if s_num(stmp):
            tmp_list.extend([i,stmp])
            fin_list.append(tmp_list)
    return fin_list

if __name__ == "__main__":
    print(list_squared(1, 250))
    print(list_squared(42, 250))
    print(list_squared(835,5523))