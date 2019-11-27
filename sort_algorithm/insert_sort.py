import random


def insert_sort(data):
    for i in range(1,len(data)):
        tmp = data[i] # 记录每次来的牌的值
        j = i - 1 # 已经排好的牌的最后一个位置
        # 新来的牌和前面已经排好序的牌比大小，
        # 如果前面的牌比他大，前面的大牌向后挪一位
        while j >= 0 and data[j] > tmp:
            data[j+1] = data[j]
            j = j - 1
        # 最后找到一个比新牌小的位置，将新牌放到这个元素后面的位置
        data[j+1] = tmp


if __name__ == '__main__':
    data = list(range(1, 12))
    random.shuffle(data)
    print(data)

    insert_sort(data)
    print(data)