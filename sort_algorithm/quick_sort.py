import random

def quick_sort(data,left,right):
    if left < right:
        mid = partition(data,left,right)
        quick_sort(data,left,mid-1)
        quick_sort(data,mid+1,right)

def partition(data,left,right):
    tmp = data[left]
    while left < right:
        while left < right and data[right] >= tmp:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= tmp:
            left += 1
        data[right] = data[left]
    data[left] = tmp
    return left


if __name__ == '__main__':

    data = list(range(1,12))
    random.shuffle(data)
    print(data)

    quick_sort(data,0,len(data)-1)
    print(data)