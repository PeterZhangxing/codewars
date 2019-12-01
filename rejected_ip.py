#!/usr/bin/python3.5

import time,os

def create_rejected_ip_list(log_file_name,blocked_file_nme):
    '''
    查询某日志文件中，1分钟内，出现次数超过20次的ip，
    并且将ip加入到指定的黑名单中。
    :param log_file_name:
    :param blocked_file_nme:
    :return:
    '''
    pin = 0
    while True:
        ip_list = []
        input_file = open(log_file_name,'r')
        input_file.seek(pin)
        for line in input_file:
            if line == '\n':
                continue
            ip = line.split()[0]
            ip_list.append(ip)
        ip_set = set(ip_list)
        for new_ip in ip_set:
            if ip_list.count(new_ip) > 20:
                with open(blocked_file_nme,'a',encoding='utf-8') as f:
                    f.write(new_ip+" : "+str(ip_list.count(new_ip))+'\n')
                    print('%s should be put in the blocked_ip list'%(new_ip))
        pin = input_file.tell()
        time.sleep(60)


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    log_file = os.path.join(BASE_DIR,'statics','access.log')
    blocked_file = os.path.join(BASE_DIR,'statics','blocked_ip.txt')

    create_rejected_ip_list(log_file,blocked_file)