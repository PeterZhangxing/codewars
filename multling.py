#!/usr/bin/python3.5

def accum(s):
    li = list(s)
    reps = []
    for i,item in enumerate(li):
        item = item.lower()
        reps.append(item.upper()+item*(i))
    return "-".join(reps)

if __name__ == "__main__":
    result = accum("tyuiuiuist")
    print(result)
