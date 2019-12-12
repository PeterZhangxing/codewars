
class CommonHelper(object):

    @staticmethod
    def readQSS(style):
        with open(style,'r') as f:
            return f.read()