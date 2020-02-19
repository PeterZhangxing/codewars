
class QssFileDealer(object):

    @staticmethod
    def set_app_qss(app,qss_file):
        with open(qss_file,'r') as f:
            qss_content = f.read()
            app.setStyleSheet(qss_content)