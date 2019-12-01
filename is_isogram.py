#!/usr/bin/python3.5

def is_isogram(strings):
    strings = strings.lower()
    ll = len(list(strings))
    sl = len(set(strings))
    if sl < ll:
        return False
    return True

if __name__ == "__main__":
    print(is_isogram('fucking'))
    print(is_isogram('moOse'))

