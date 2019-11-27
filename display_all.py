#!/usr/bin/python3.5

import os

def dis_dir(dirname,j=0):
    i = len(os.path.basename(dirname))+3
    v = i + j
    print(" "*j,"<"+os.path.basename(dirname)+">:")
    for file_name in os.listdir(dirname): # list出来的文件和文件夹都是相对路径
        file_name = os.path.join(dirname, file_name) # 拼接出一个绝对路径
        if os.path.isdir(file_name): # 只能判断完全路径是否为文件夹，相对路径不行
            dis_dir(file_name,v)
        else:
            print(" "*v,os.path.basename(file_name))


if __name__ == "__main__":
    dis_dir(os.getcwd())