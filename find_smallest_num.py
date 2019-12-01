import time

def cal_run_time(func):
    def inner(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        print(end_time-start_time)
        return res
    return inner

def juge_num(num):
    for i in range(2,num//2+1):
        if num % i == 0:
            return False
    else:
        return True

def get_num_ele(num):
    ele_li = []
    if juge_num(num):
        return [1,num]

    while True:
        if juge_num(num) and num != 1:
            ele_li.append(num)
            break
        for i in range(2,num//2+1):
            if num % i == 0 and juge_num(i):
                ele_li.append(i)
                num = num//i
                break

    return sorted(ele_li)

def found_all_sushu(num):
    sushu_li = []
    for i in range(2,num+1):
        if juge_num(i):
            sushu_li.append(i)
    return sushu_li

def get_sushumul_res(num):
    li = found_all_sushu(num)
    res = 1
    for i in li:
        res *= i
    return res

def find_unmod(num):
    mul_res = get_sushumul_res(num)
    unmod_li = []
    for i in range(2,num+1):
        if mul_res % i != 0:
            unmod_li.append(i)
    return unmod_li

def get_mini_num(num):
    mydict = {}
    unmod_li = find_unmod(num)
    for i in unmod_li:
        tmp_dict = {}
        for j in get_num_ele(i):
            tmp_dict.setdefault(j,0)
            tmp_dict[j] += 1
        mydict[i] = tmp_dict
    # print(mydict)

    count_dict = {}
    for k,v in mydict.items():
        for key,value in v.items():
            count_dict.setdefault(key,value)
            if count_dict[key] < value:
                count_dict[key] = value
    # print(count_dict)

    extra_mul_num = 1
    for k,v in count_dict.items():
        extra_mul_num *= k**(v-1)

    return extra_mul_num * get_sushumul_res(num)

@cal_run_time
def main(num):
    res = get_mini_num(num)
    return res

if __name__ == '__main__':
    res = main(140)
    print(res) # 232792560 9699690