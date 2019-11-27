#!/usr/bin/python3.5

def find_uniq(arr):
    count = {}
    arr_len = len(arr)
    count[arr[0]] = 0

    for item in arr:
        if item != arr[0]:
            count[item] = 0

    i = 0
    while i < arr_len:
        j = 0
        if count[arr[i]] == 0:
            while j < arr_len:
                if arr[i] == arr[j]:
                    count[arr[i]] += 1
                j += 1
        i += 1

    for k,v in count.items():
        if v == 1:
            return k
        else:
            print("No unique element in the list!")
            return count


if __name__ == "__main__":
    print(find_uniq([ 3, 10, 3, 3, 3 ,5,12,5,6,7,7,7,32,12,10]))