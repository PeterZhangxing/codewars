#!/usr/bin/python3.5

li = ["1","test","last","9","transfer","234","qustions","90"]
dig_li = []

for i,v in enumerate(li):
    if v.isdigit():
        dig_li.append(i)

print(dig_li)

j = 0
for i in dig_li:
    i = i-j
    del li[i]
    j += 1

print(li)