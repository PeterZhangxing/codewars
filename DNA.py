#!/usr/bin/python3.5

def DNA_strand(dna):
    DNA_dic = {'A':'T','C':'G','T':'A','G':'C'}
    res = ""
    for st in dna:
        rs = DNA_dic[st]
        res = res + rs
    return res

if __name__ == "__main__":
    print(DNA_strand("AAAA"))