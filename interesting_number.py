#!/usr/bin/python3.5

import re

def re_compare(key):
    sr1 = r"[1-9][0]+$"
    sr2 = r"[1]+$|[2]+$|[3]+$|[4]+$|[5]+$|[6]+$|[7]+$|[8]+$|[9]+$"
    # sr3 = r"^(.?)(.?)(.?)(.?)(.?)(.?)(.?)(.?)(.?).?\9\8\7\6\5\4\3\2\1$"
    pat1 = re.compile(sr1)
    pat2 = re.compile(sr2)
    # pat3 = re.compile(sr3)
    pats = [pat1,pat2]
    for pat in pats:
        if re.match(pat,key):
            print(re.match(pat1,key).group(0))
            return True
        else:
            print('no matched string')
            return  False

def reversable(key):
    res = reversed(key)
    tag = None
    j = 0
    for i in res:
        if i != key[j]:
            tag = False
            break
        else:
            tag = True
            j += 1
    return tag

key = '131242143'
key1 = '431111111134'