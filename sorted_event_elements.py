#!/usr/bin/python3.5

def sort_event_li(*args):
    '''
    只是排序一个列表中的奇数，偶数位置不变
    :param args:
    :return:
    '''
    temp_li = args[0]
    event_li = sorted([x for x in temp_li if x%2!=0])

    j = 0
    for i,v in enumerate(temp_li):
        if v%2!=0:
            temp_li[i] = event_li[j]
            j += 1
        else:
            continue

    return temp_li

# print(input_li) # [2, 1, 6, 3, 5, 4, 7]

if __name__ == '__main__':

    input_li = [2,7,6,1,5,4,3]
    res = sort_event_li(input_li)
    print(res)