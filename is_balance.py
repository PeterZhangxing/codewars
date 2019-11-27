#!/usr/bin/python3.5

def is_balance(left,right):
    left_weight = left.count('!')*2 + left.count('?')*3
    right_weight = right.count('!')*2 + right.count('?')*3
    res = left_weight - right_weight

    if res > 0:
        return "Left"
    elif res < 0:
        return "Right"
    else:
        return "Balance"

if __name__ == '__main__':
    res = is_balance("!!","??")
    print(res)