#!/usr/bin/python3.5

import configparser

conf_file = configparser.ConfigParser()

while True:
    username = input('username: ')
    if username == 'quit':
        break
    password = input('password: ')
    qotation = input('qotation: ')
    if conf_file.has_section(username):
        print("s% exist!" %username)
        continue
    else:
        conf_file.add_section(username)
        conf_file.set(username,'password',password)
        conf_file.set(username,'qotation',qotation)

with open('account.ini','a') as f:
    conf_file.write(f)
