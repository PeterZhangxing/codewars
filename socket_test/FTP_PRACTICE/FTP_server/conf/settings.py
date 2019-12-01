#!/usr/bin/python3.5

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACC_PATH = os.path.join(BASE_DIR,'conf','account.ini')
LOG_PATH = os.path.join(BASE_DIR, 'logger', 'ftp_server.log')
LOG_FORMAT = "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"

Listen_IP = '127.0.0.1'
Listen_Port = 8009
Ip_Port = (Listen_IP,Listen_Port)