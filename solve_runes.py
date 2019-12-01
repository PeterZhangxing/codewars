#!/usr/bin/python3.5

# import re
#
# def solve_runes(runes):
#     # exp = r'(?P<opn1>[-]?[?,0-9]+)(?P<op>[*,-,+]{1})(?P<opn2>[-]?[?,0-9]+)=(?P<res>[-]?[?,0-9]+)'
#
#     exp = r'([-]?[?,\d]+)'
#     op_exp = r'([-,+,*])'
#     cexp = re.compile(exp)
#     coexp = re.compile(op_exp)
#
#     li = []
#     while cexp.search(runes):
#         opn = cexp.search(runes).group()
#         li.append(opn)
#         runes = runes.replace(opn,"",1)
#
#     opn1 = li[0]
#     opn2 = li[1]
#     res = li[2]
#     op = coexp.search(runes).group()
#
#     if not opn1.strip('-').startswith('?') and not opn2.strip('-').startswith('?') and not res.strip('-').startswith('?'):
#         for i in range(0, 10):
#             tmp_res = eval(opn1.replace('?',str(i)) + op + opn2.replace('?',str(i)))
#             if res.replace('?',str(i)) == str(tmp_res) and str(i) not in runes:
#                 return i
#         return -1
#     else:
#         for j in range(1, 10):
#             tmp_res = eval(opn1.replace('?', str(j)) + op + opn2.replace('?', str(j)))
#             if res.replace('?',str(j)) == str(tmp_res) and str(j) not in runes:
#                 return j
#         return -1

# import re
#
# def solve_runes(runes):
#     for d in sorted(set("0123456789") - set(runes)):
#         toTest = runes.replace("?",d)
#         if re.search(r'([^\d]|\b)0\d+', toTest): continue
#         l,r = toTest.split("=")
#         if eval(l) == eval(r): return int(d)
#     return -1

import re

def solve_runes(runes):
    exp = r'(?P<opn1>[-]?[?,0-9]+)(?P<op>[-,+,*])(?P<opn2>[-]?[?,0-9]+)=(?P<res>[-]?[?,0-9]+)'
    cexp = re.compile(exp)

    opn1 = cexp.search(runes).group('opn1')
    opn2 = cexp.search(runes).group('opn2')
    res = cexp.search(runes).group('res')
    op = cexp.search(runes).group('op')

    if op == "*":
        if opn1 == "?" or opn2 == "?":
            if res == "?":
                return 0
    elif op == "-" or op == "+":
        if opn1 == "?" and opn2 == "?" and res == "?":
            return 0

    if not opn1.strip('-').startswith('?') and not opn2.strip('-').startswith('?') and not res.strip('-').startswith('?'):
        for i in range(0, 10):
            tmp_res = eval(opn1.replace('?',str(i)) + op + opn2.replace('?',str(i)))
            if int(res.replace('?',str(i))) == tmp_res and str(i) not in runes:
                return i
        return -1
    else:
        for i in range(1, 10):
            tmp_res = eval(opn1.replace('?', str(i)) + op + opn2.replace('?', str(i)))
            if int(res.replace('?',str(i))) == tmp_res and str(i) not in runes:
                return i
        return -1


if __name__ == "__main__":
    print(solve_runes("19--45=5?"))
    print(solve_runes("??*??=302?"))
    print(solve_runes("123*45?=5?088"))
    print(solve_runes("-5?*-1=5?"))
    print(solve_runes("?*11=??"))
    print(solve_runes("?*11=?"))