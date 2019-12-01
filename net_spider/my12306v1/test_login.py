import requests
from bs4 import BeautifulSoup
import json,time
import base64
from myaccount import username,password

mysession = requests.Session()

myheader = {
    'Referer': 'https://kyfw.12306.cn/otn/login/init',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}

help_info = '''
'请输入验证码:
        #================================================================
        # 根据打开的图片识别验证码后手动输入,输入正确验证码对应的位置,例如:2 5   #
        # ---------------------------------------                       #
        #         |         |         |                                 #
        #    0    |    1    |    2    |     3                           #
        #         |         |         |                                 #
        # ---------------------------------------                       #
        #         |         |         |                                 #
        #    4    |    5    |    6    |     7                           #
        #         |         |         |                                 #
        # ---------------------------------------                       #
        #================================================================
--------------------- 
'''

uamtk = None

############### 第一步
# 获取验证码图片
# https://kyfw.12306.cn/passport/captcha/captcha-image64?login_site=E&module=login&rand=sjrand&

# tmp_time = str(int(time.time()*1000))
def get_code_pic():
    get_code_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image64?' \
                   'login_site=E&module=login&rand=sjrand&0.24433916188362326'

    # 获取验证码图片base64编码
    check_pic_info = mysession.request(
        method='GET',
        url=get_code_url,
        headers=myheader
    )
    check_pic_b64 = json.loads(check_pic_info.content)['image']
    # 解码base64编码的图片，并保存到本地
    imagedata = base64.b64decode(check_pic_b64)
    with open('check_pic.jpg','wb') as img_f:
        img_f.write(imagedata)

    print(help_info)
    check_code_pos = input('请输入验证码位置，以","分割[例如2 5]:').strip()
    return check_code_pos


############### 第二步
# 发送验证码

def send_ckeck_code():
    check_code_pos = get_code_pic()
    check_code_pos_li = check_code_pos.split(' ')
    # pos_code_li = ['35,35','105,35','175,35','245,35','35,105','105,105','175,105','245,105']
    pos_code_li = ['38,46','108,42','184,40','251,44','43,117','110,111','183,112','259,112']
    check_code_li = []
    for i in check_code_pos_li:
        check_code_li.append(pos_code_li[int(i)])
    check_code = ','.join(check_code_li)
    print(check_code)

    send_code_url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
    code_data = {
        'answer': check_code,
        'login_site': 'E',
        'rand': 'sjrand'
    }

    code_resp = mysession.request(
        method='POST',
        url=send_code_url,
        headers=myheader,
        data=code_data
    )
    check_code_res = json.loads(code_resp.content)
    print(check_code_res)
    if check_code_res['result_code'] == '4':
        print('验证码输入正确')
        return True
    else:
        print('验证码输入错误，重试！')
        return False


############### 第三步
# 发送用户名和密码

def auth_user_account():
    while not send_ckeck_code():
        send_ckeck_code()

    send_auth_url = 'https://kyfw.12306.cn/passport/web/login'

    login_data = {
        'username': username,
        'password': password,
        'appid': 'otn',
    }

    login_resp = mysession.request(
        method='POST',
        url=send_auth_url,
        headers=myheader,
        data=login_data
    )
    auth_res = json.loads(login_resp.content)
    print(auth_res)
    if auth_res['result_code']:
        auth_user_account()
    global uamtk
    uamtk = auth_res['uamtk']
    print('用户登录成功')


if __name__ == '__main__':
    auth_user_account()