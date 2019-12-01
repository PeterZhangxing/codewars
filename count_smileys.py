#!/usr/bin/python3.5

def count_smileys(arr):
    count = 0
    for a in arr:
        al = list(a)
        if len(al) == 2:
            if al[0] in [':',';'] and al[1] in [')','D']:
                count += 1
        elif len(al) == 3:
            if al[0] in [':', ';'] and al[1] in ['-', '~'] and al[2] in [')', 'D']:
                count += 1
    return count

if __name__ == "__main__":
    print(count_smileys([':D',':~)',';~D',':)']))
