#!/usr/bin/python3.5

import os,re

def findword(dir,ignore_list):
    if not os.path.isdir(dir):
        return '%s is not a valid dirname!'
    file_list = os.listdir(dir)
    re_obj = re.compile(r'\b(\w+)\b')
    for file in file_list:
        file_path = os.path.join(dir,file)
        # splitext可以获取路径中文件的后缀名，以'.'作为分割符号，并且包含'.'
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1] == '.txt':
            with open(file_path,'r',encoding='utf-8') as f:
                data = f.read()
                words = re_obj.findall(data)
                word_dict = {}
                for word in words:
                    word = word.lower()
                    if word in ignore_list:
                        continue
                    if word in  word_dict.keys():
                        word_dict[word] += 1
                    else:
                        word_dict[word] = 1

            anslist = sorted(word_dict.items(),key=lambda x:x[1],reverse=True)
            print('file:%s->the word appeared mostly: %s'%(file,anslist[0]))


if __name__ == "__main__":

    ignore_list = ['a', 'the', 'to', 'an', 'is', 'am', 'are', 'were', 'was', 'in', 'on', 'at','of','and','or']
    findword('E:\PycharmProjects\codewars\statics',ignore_list)

    # print(os.path.splitext(r'E:\PycharmProjects\codewars\statics\test.txt'))
    # # ('E:\\PycharmProjects\\codewars\\statics\\test', '.txt')
    #
    # print(os.path.basename(r'E:\PycharmProjects\codewars\statics\test.txt').split('.'))
    # # ['test', 'txt']