#!/usr/bin/python3.5

import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import mylogger

if __name__ == "__main__":
    my_log = mylogger.MyLogger()
    my_log.logger.warning('this is a test1')