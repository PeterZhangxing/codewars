#!/usr/bin/python3.5

import logging,os
from conf import settings

class MyLogger(object):

    def __init__(self):
        # 第一步，创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        # 第二步，创建一个handler，用于写入日志文件
        logfile = settings.LOG_PATH
        fh = logging.FileHandler(logfile, mode='a')
        fh.setLevel(logging.DEBUG)

        # 第三步，再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.WARNING)

        # 第四步，定义handler的输出格式
        formatter = logging.Formatter(settings.LOG_FORMAT)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 第五步，将logger添加到handler里面
        logger.addHandler(ch)
        logger.addHandler(fh)

        self.logger = logger
