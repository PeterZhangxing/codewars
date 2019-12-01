import time

def time_dec(func):
    def inner_func(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        time_spend = end_time - start_time
        return res,time_spend,func.__name__
    return inner_func

@time_dec
def half_find(data_li,data):
    '''
    二分查找算法，实现在有序列表中查找某个数
    :param data_li:
    :param data:
    :return:
    '''
    start = 0
    end = len(data_li)-1
    while start <= end:
        mid = (start+end)//2
        if data_li[mid] == data:
            return mid,data_li[mid]
        elif data_li[mid] > data:
            end = mid-1
        else:
            start = start+1
    return

@time_dec
def sequence_find(data_li,data):
    '''
    顺序查找列表中数据的位置
    :param data_li:
    :param data:
    :return:
    '''
    for i in range(len(data_li)):
        if data_li[i] == data:
            return i,data_li[i]
    return


if __name__ == '__main__':

    data_li = list(range(1,100000000))
    res1 = half_find(data_li,12432011)
    print(res1)

    res2 = sequence_find(data_li,12432011)
    print(res2)