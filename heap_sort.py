import random

def sift_heap(data,low,high):
    i = low
    j = 2*i+1
    tmp = data[i]
    while j <= high:
        if j < high and data[j] > data[j+1]:
            j = j+1
        if tmp > data[j]:
            data[i] = data[j]
            i = j
            j = 2*i+1
        else:
            break
    data[i] = tmp

def heap_sort(data):
    for i in range(len(data)//2-1,-1,-1):
        sift_heap(data,i,len(data)-1)
    for i in range(len(data)-1,-1,-1):
        data[0],data[i] = data[i],data[0]
        sift_heap(data,0,i-1)


if __name__ == '__main__':
    data = list(range(1, 12))
    random.shuffle(data)
    print(data)

    heap_sort(data)
    print(data)