#!/usr/bin/python3.5

def move_zeros(array):
    count = 0
    i = 0
    while i < len(array):
        if array[i] == 0 and type(array[i]) is not bool:
            count += 1
            del array[i]
            continue
        i += 1

    for i in range(count):
        array.append(0)
    return array


if __name__ == "__main__":
    print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))