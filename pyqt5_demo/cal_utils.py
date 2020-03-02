
from PyQt5.QtCore import *


class Calculator(QObject):
    show_content = pyqtSignal(str)

    def __init__(self,parent):
        super(Calculator, self).__init__(parent)
        self.key_models = []

    def get_result(self):
        # print('get_result')
        expression = ""
        for model in self.key_models:
            expression += model["title"]
        result = eval(expression)
        print(result)
        return str(result)

    def parse_key_model(self,key_model):
        # print(key_model)
        # self.show_content.emit(key_model.get('title'))
        key_title = key_model.get('title')
        key_role = key_model.get('role')
        # print(key_title,key_role)

        if key_role == 'clear':
            self.key_models = []
            self.show_content.emit('0.0')
            self.key_models.append({'title': '0', 'role': 'num'})
        elif key_role == 'calculate':
            if len(self.key_models) == 3:
                result = self.get_result()
                self.show_content.emit(result)
                self.key_models.clear()
                self.key_models.append({'title': result, 'role': 'num'})
        elif key_role == 'operator':
            if len(self.key_models) != 0:
                if self.key_models[-1].get('role') == 'num':
                    if len(self.key_models) == 3:
                        if self.key_models[-1].get('titlt') == '0.':
                            self.key_models[-1]['titlt'] = '0'
                        result = self.get_result()
                        self.key_models.append({'title':result,'role':'num'})
                        self.show_content.emit(result)
                    else:
                        self.key_models.append(key_model)
                elif self.key_models[-1].get('role') == 'operator':
                    self.key_models[-1]['titlt'] = key_title
        elif key_role == 'num':
            if len(self.key_models) == 0:
                if key_title == '.':
                    key_model = {'title':'0.','role':'num'}
                elif key_title in ['+/-','%']:
                    return None
                self.key_models.append(key_model)
                self.show_content.emit(self.key_models[-1]["title"])
            else:
                if self.key_models[-1].get('role') == 'num':
                    if key_title == '.':
                        if not self.key_models[-1].get('title').__contains__('.'):
                            self.key_models[-1]['title'] += key_title
                    elif key_title == '+/-' and self.key_models[-1].get('title') != '0.':
                        self.key_models[-1]['title'] = str(float(self.key_models[-1]['title']) * (-1))
                    elif key_title == '%' and self.key_models[-1].get('title') != '0.':
                        self.key_models[-1]['title'] = str(float(self.key_models[-1]['title']) * 0.01)
                    else:
                        if self.key_models[-1]["title"] != "0":
                            self.key_models[-1]["title"] += key_title
                        else:
                            self.key_models[-1]["title"] = key_title
                    self.show_content.emit(self.key_models[-1]["title"])
                elif self.key_models[-1].get('role') == 'operator':
                    if key_title not in ['+/-','%','.']:
                        self.key_models.append(key_model)
                        self.show_content.emit(self.key_models[-1]["title"])
                    else:
                        if key_title == '.':
                            key_model = {'title': '0.', 'role': 'num'}
                            self.key_models.append(key_model)
                            self.show_content.emit(self.key_models[-1]["title"])