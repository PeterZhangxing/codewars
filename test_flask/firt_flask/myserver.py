from flask import Flask,url_for,redirect,current_app
from werkzeug.routing import BaseConverter

app = Flask(__name__,static_url_path='/static')

app.config['DEBUG'] = True

@app.route('/index',methods=['post','get'])
def index():
    return 'index is ok'

# @app.route('/order/<page_num>',methods=['post','get'])
@app.route('/order/<int:page_num>',methods=['post','get'])
def order_display(page_num):
    print(type(page_num))
    return 'page %s'%page_num

class MyReConvertor(BaseConverter):
    def __init__(self,url_map,regx):
        super(MyReConvertor, self).__init__(url_map)
        self.regex = regx

    def to_python(self, value):
        print(value)
        return value
        # return '18687027119'

    def to_url(self, value):
        print(value)
        return value

app.url_map.converters['re'] = MyReConvertor

@app.route('/sendto/<re(r"1[3578]\d{9}"):mobile>')
def send_mail_to(mobile):
    return "mobile phone number is %s"%mobile

@app.route('/redirect')
def test_redirect():
    re_url = url_for('send_mail_to',mobile='13529209726')
    return redirect(re_url)

if __name__ == '__main__':
    app.run(host='10.1.1.129', port=8080)