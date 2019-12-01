#!/usr/bin/python3.7


def find_noreapt_str_li(one_str):
    '''
    找出该字符串中，所有组成字符不重复的子字符串
    '''
    res_list=[]
    length=len(one_str)

    for i in range(length):
        tmp=one_str[i]
        for j in range(i+1, length):
            if one_str[j] not in tmp:
                tmp+=one_str[j]
            else:
                break
        res_list.append(tmp)

    return res_list


def find_longest_str(input_str):
    '''
    从列表中，找出一个最长的不重复字符串
    :param input_str:
    :return:
    '''
    res_li = find_noreapt_str_li(input_str)

    res = ''
    for i, v in enumerate(res_li):
        if len(v) > len(res):
            res = v

    return res


if __name__ == '__main__':

    test_str = 'abcdefabcdwfsdgfewqwet'
    res = find_longest_str(test_str)
    print(res)