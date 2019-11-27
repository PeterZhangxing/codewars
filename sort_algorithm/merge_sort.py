import random
import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result
    return wrapper

def merge_once(data,left,mid,right):
    i = left
    j = mid+1
    tmp_li = []
    while i <= mid and j <= right:
        if data[i] < data[j]:
            tmp_li.append(data[i])
            i += 1
        else:
            tmp_li.append(data[j])
            j += 1
    while i <= mid:
        tmp_li.append(data[i])
        i += 1
    while j <= right:
        tmp_li.append(data[j])
        j += 1
    data[left:right+1] = tmp_li

def merge_sort(data,left,right):
    if left < right:
        mid = (left+right)//2
        merge_sort(data,left,mid)
        merge_sort(data,mid+1,right)
        merge_once(data,left,mid,right)

@cal_time
def my_merge_sort(data):
    return merge_sort(data,0,len(data)-1)


if __name__ == '__main__':
    data = list(range(1, 121121))
    random.shuffle(data)
    print(data)

    my_merge_sort(data)
    print(data)