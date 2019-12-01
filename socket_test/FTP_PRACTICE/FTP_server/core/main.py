#!/usr/bin/python3.5

import optparse,socketserver
from conf import settings
from core import server
from core import mylogger

my_log = mylogger.MyLogger()

class ArgvHandler(object):

    def __init__(self):
        self.op = optparse.OptionParser()
        options,args = self.op.parse_args()
        self.verify_args(options,args)

    def verify_args(self,options,args):
        if hasattr(self,args[0]):
            func = getattr(self,args[0])
            func()
        else:
            self.op.print_help()

    def start(self):
        ser = socketserver.ThreadingTCPServer(settings.Ip_Port,server.MyServerHandler)
        # print('FTP server has started...')
        my_log.logger.critical('FTP server has started...')
        ser.serve_forever()
