import random
import time

def outer(func):
    def inner(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        during = end_time - start_time
        return res,during
    return inner

@outer
def bubble_sort(data_li):
    '''
    冒泡排序算法
    :param data_li:
    :return:
    '''
    for i in range(len(data_li)-1):
        ex_flag = False
        for j in range(len(data_li)-i-1):
            if data_li[j] < data_li[j+1]:
                data_li[j+1],data_li[j] = data_li[j],data_li[j+1]
                ex_flag = True
        if not ex_flag:
            break
    return data_li

@outer
def find_sort(data_li):
    '''
    查找排序，每次从剩余的列表元素中找到最大的或者最小的，放到开始比较的位置
    :param data_li:
    :return:
    '''
    for i in range(len(data_li)):
        smallest_loc = i
        for j in range(i+1,len(data_li)):
            if data_li[j] < data_li[smallest_loc]:
                smallest_loc = j
        data_li[i],data_li[smallest_loc] = data_li[smallest_loc],data_li[i]
    return data_li

@outer
def sys_sort(data_li):
    '''
    系统自带的排序
    :param data_li:
    :return:
    '''
    data_li.sort()
    return data_li


if __name__ == '__main__':

    data_li = list(range(1,12111))
    # print(data_li)

    # 乱序排列数组中的元素
    random.shuffle(data_li)
    # print(data_li)

    # data_li = bubble_sort(data_li)
    # print(data_li) # 30.46012282371521

    # data_li = find_sort(data_li)
    # print(data_li) # 9.175311803817749

    data_li = sys_sort(data_li)
    print(data_li) # 0.0039980411529541016