#!/usr/bin/python3.5

def sort_array(source_array):
    if not source_array:
        return source_array

    tmp_li = []
    for i,v in enumerate(source_array):
        if v % 2 != 0:
            tmp_li.append(v)
    final_li = sorted(tmp_li)
    final_li.reverse()

    for j,k in enumerate(source_array):
        if k % 2 != 0:
            source_array[j] = final_li.pop()

    return source_array

if __name__ == "__main__":
    print(sort_array([5, 3, 1, 8, 0]))
    print(sort_array([0,5, 3, 2, 8, 1, 4]))