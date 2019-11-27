import requests
from bs4 import BeautifulSoup
import json,time
import base64
import urllib.parse
import re
from myaccount import username,password

mysession = requests.Session()

myheader = {
    'Referer': 'https://kyfw.12306.cn/otn/login/init',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}

help_info = '''
'请输入验证码:
        #================================================================
        # 根据打开的图片识别验证码后手动输入,输入正确验证码对应的位置,例如:2 5  #
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
    check_code_pos = input('请输入验证码位置，以"空格"分割[例如2 5]:').strip()
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
    # print(check_code_res)
    if check_code_res['result_code'] == '4':
        print('验证码输入正确')
        return True
    else:
        print('验证码输入错误，重试！')
        return False


############### 第三步
# 发送用户名和密码,实现用户的真正登录

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
    # print(auth_res)

    if auth_res['result_code']:
        print('用户验证失败，将会重新验证')
        time.sleep(3)
        auth_user_account()

    global uamtk
    uamtk = auth_res['uamtk']

    print('用户验证成功')

    # 成功登录前要发送的请求1
    before_index_url1 = 'https://kyfw.12306.cn/otn/login/userLogin'
    before_index_data1 = {
        '_json_att':'',
    }

    before_index_resp1 = mysession.request(
        method='POST',
        url=before_index_url1,
        headers=myheader,
        data=before_index_data1
    )

    # 成功登录前要发送的请求2
    before_index_url2 = 'https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin'
    before_index_resp2 = mysession.request(
        method='GET',
        url=before_index_url2,
        headers=myheader,
    )

    # 成功登录前要发送的请求3
    before_index_url3 = 'https://kyfw.12306.cn/passport/web/auth/uamtk'
    before_index_data3 = {
        'appid':'otn',
    }

    before_index_resp3 = mysession.request(
        method='POST',
        url=before_index_url3,
        headers=myheader,
        data=before_index_data3
    )

    tk = json.loads(before_index_resp3.content.decode('utf8'))['newapptk']
    # print(before_index_resp3.content.decode('utf8'))
    # {"result_message": "验证通过", "result_code": 0, "apptk": null,
     # "newapptk": "33swVj25CrA_oIvJMcFNLI-SeCQtDU_jRhqVTQU-5R4zi1110"}

    # 成功登录前要发送的请求4
    before_index_url4 = 'https://kyfw.12306.cn/otn/uamauthclient'
    before_index_data4 = {
        'tk':tk,
    }

    before_index_resp4 = mysession.request(
        method='POST',
        url=before_index_url4,
        headers=myheader,
        data=before_index_data4
    )
    final_auth_rescode = json.loads(before_index_resp4.content.decode('utf8'))['result_code']
    '''
    print(final_auth_rescode)
    {"apptk":"Bv3B2ZBsoaUxJWbR6S5HrtazHcV0v_wUQnqf0pdMX_0cg1110",
    "result_code":0,"result_message":"验证通过","username":"张兴"}
    '''

    if not final_auth_rescode:
        # 获取个人配置信息
        pinfo_conf_url = 'https://kyfw.12306.cn/otn/login/conf'

        pinfo_conf_resp = mysession.request(
            method='POST',
            url=pinfo_conf_url,
            headers=myheader,
        )
        '''
        print(pinfo_conf_resp.content.decode('utf8'))
        {"validateMessagesShowId":"_validatorMessage","status":true,
        "httpstatus":200,
        "data":{"isstudentDate":false,"is_login_passCode":"Y",
                "is_sweep_login":"Y","psr_qr_code_result":"N",
                "login_url":"resources/login.html","name":"张兴",
                "studentDate":["2018-06-01","2018-09-30",
                               "2018-12-01","2018-12-31",
                               "2019-01-01","2019-03-31"],
                 "stu_control":52,"is_uam_login":"Y","is_login":"Y",
                 "other_control":30},
        "messages":[],"validateMessages":{}}
        '''

        # 获取首页初始化数据
        init_pinfo_url = 'https://kyfw.12306.cn/otn/index/initMy12306Api'

        init_pinfo_resp = mysession.request(
            method='POST',
            url=init_pinfo_url,
            headers=myheader,
        )
        '''
        print(init_pinfo_resp.content.decode('utf8'))
        {"validateMessagesShowId": "_validatorMessage", "status": true, "httpstatus": 200,
         "data": {"notify_way": "7", "qr_code_url": "Y",
                  "if_show_ali_qr_code": true, "isSuperUser": "N",
                  "_email": "99360681@qq.com", "user_status": "1",
                  "_is_needModifyPassword": null, "needEdit": false,
                  "member_status": "您母亲的姓名是？", "id_type_code": "1",
                  "notify_TWO_2": "完成手机双向核验，即可使用手机号码直接登录的新服务，解除您遗忘用户名的烦恼。",
                  "user_name": "张兴", "member_level": "",
                  "isCanRegistMember": true, "user_regard": "先生,上午好！",
                  "resetMemberPwd": "N", "_is_active": "Y"},
         "messages": [], "validateMessages": {}}
        '''

        return True
    return False


############### 第四步
# 查询并获取到某地的票务信息

# 存储所有符合查询条件的车次的票务信息
ticket_info_dic = {}
# 存储所有有你需要的票的列车的信息
pot_choice_dic = {}
# 存储所有有买票资格的人的个人信息
guests_info_dic = {}

def _is_authorized():
    '''
    print(pinfo_conf_resp.content.decode('utf8'))
    {"validateMessagesShowId":"_validatorMessage","status":true,
    "httpstatus":200,
    "data":{"isstudentDate":false,"is_login_passCode":"Y",
            "is_sweep_login":"Y","psr_qr_code_result":"N",
            "login_url":"resources/login.html","name":"张兴",
            "studentDate":["2018-06-01","2018-09-30",
                           "2018-12-01","2018-12-31",
                           "2019-01-01","2019-03-31"],
             "stu_control":52,"is_uam_login":"Y","is_login":"Y",
             "other_control":30},
    "messages":[],"validateMessages":{}}
    '''
    # 获取个人配置信息
    pinfo_conf_url = 'https://kyfw.12306.cn/otn/login/conf'
    pinfo_conf_resp = mysession.request(
         method='POST',
         url=pinfo_conf_url,
         headers=myheader,
    )
    # print(pinfo_conf_resp.content.decode('utf8'))
    _is_login = json.loads(pinfo_conf_resp.content.decode('utf8'))['data']['is_login']
    if _is_login == "Y":
        print('you have been authorised')
        return True
    print('you need to login')
    return False


def find_tickets():
    '''
    获取票务信息
    :return:
    '''
    if _is_authorized():
        train_date = '2019-02-03'
        from_station = 'KMM'
        to_station = 'AXM'
        purpose_codes = 'ADULT'
        find_left_url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ'
        find_left_resp = mysession.request(
            method='GET',
            url=find_left_url,
            headers=myheader,
            params={
                'leftTicketDTO.train_date':train_date,
                'leftTicketDTO.from_station':from_station,
                'leftTicketDTO.to_station':to_station,
                'purpose_codes':purpose_codes,
            }
        )
        '''
        print(find_left_resp.content.decode('utf8'))
        {
        "data": {
            "flag": "1", 
            "map": {
                "AXM": "玉溪", 
                "KMM": "昆明", 
                "KOM": "昆明南"
            }, 
            "result": [
                "dAGc4MuT8VG%2Bl0zQx5JSult588oFV5JG%2FUMl6UfBAKyORD
                soib02eD%2FZIpkE7ORRvdN9z1I7FtDf%0A1N12dh0c7AsLYk0P
                8g%2BijC%2FbKisS%2FeaoWXZDOKPI9DP7b0AgcgQgu%2FAsM8Y
                jTrXqhlWQswXKmbxV%0Ac1IpRaOGxsfVOO1fNSESaQj7d291r43
                %2Busk4SEy5r9sDIhL84XwFSpeQj65JfjnRnlHHp47CydXT%0AK
                ZgDGG33s24U0I9KA%2BdHN%2BAdjMcT6GLPyy%2BZgEvOgL3P%2
                FzRyBv1VwkKCkqwCG1Zm%2BBuxKfrxni9Q%0AnG6PTw%3D%3D
                |预订|240000K63503|K638|BXP|AXM|KMM|AXM|05:30|06:48|01:18|Y|
                MPApPZjZIcgAnsZgHdx1X6m6GYIznx2WfvwK%2FtkeBnOv8uOSPSSD1BZ4cHU%3D|
                20190203|3|P4|32|34|0|0||||无|||有||有|有|||||10401030|1413|0|0", 
                "5qjHid908We4EnpSVSRx2r7UWUzzneSFfcNk4Khdx3oT47qqdnU
                IsmGGnHxmkfcl95dylN1HTXrX%0AprGBVOENVy3Et7DQix8G9J%2
                F%2F%2FyKxjpBLyybRadyk6Sfau8oDCCXHYC3KBXjW%2Bs3Ha%2B
                iEdiydlJuW%0ALPSpbgg3TbKAZqV7TR0GWN7HpC4PQS7oDZgqqba
                y0SQF84xZPDulK82xa9NjOuVURBLp0qPiVzEt%0AEL4hqPFqVQ7S
                GGKGZNtg6hAAC2sJMrskfKZs7eVg7Z6QeBCLDuTRcDByVi8f14Dk
                nTGdXiQ%3D|预订|80000D864101|D8641|KOM|AXM|KOM|AXM|
                08:10|08:42|00:32|Y|eUaqIGGWPkMsitMRZx5YtakHoxaNBC
                H2gPU8tgIgOAm04Szv|20190205|3|M1|01|02|0|0|||||||||||有|18|5||O1M191|OM9|1|0", 
                ]
            }, 
            "httpstatus": 200, 
            "messages": "", 
            "status": true
        }
        '''
        '''
        每个车次中列表值的意义：
        0 ：mysecretstr 作为车次的唯一标识符的一大串编码
        3 : K638 车次
        4 : BXP 北京西 列车始发站
        5 : AXM 玉溪 列车终点站
        6 : KMM 昆明 票上出发站
        7 : AXM 玉溪 票上到达站
        8 : 05:30 出发时间
        9 : 06:48 到达时间
        10 : 01:18 历时
        12 : L1WdEcGGlrmDls%2BRCRc9lQPWlFvDo63hMXOqO5bfH9iRBnnZ 后面会用到
        13 : 20190203 所要购买的车票的日期
        23 : 2 软卧一等卧
        24 :   软座
        25 : 
        26 : 有 无座
        27 : 
        28 : 有 硬卧二等卧
        29 : 有 硬座
        '''

        global ticket_info_dic
        find_left_result_li = json.loads(find_left_resp.content.decode('utf8'))['data']['result']
        for i in range(len(find_left_result_li)):
            tmp_li = find_left_result_li[i].split('|')
            ticket_info_dic[tmp_li[3]] = tmp_li
            # for j in range(len(tmp_li)):
            #     tmp_item = tmp_li[j]
            #     print(j,':',tmp_item)
        # print(ticket_info_dic)
        global pot_choice_dic
        for k,v in ticket_info_dic.items():
            # 只将有硬座的车次加入字典，以后可以根据需要修改为有其他座位或者卧铺的
            if v[29] == '有':
                pot_choice_dic[k] = v
            elif v[29].isdigit():
                if int(v[29]) > 0:
                    pot_choice_dic[k] = v
        # print(pot_choice_dic)
    else:
        print('登录未成功')
        auth_user_account()


def get_ticket():
    find_tickets()
    # 有车次有票，买票
    if pot_choice_dic:
        # 第一次请求
        get_tickets_url1 = 'https://kyfw.12306.cn/otn/login/checkUser'
        get_tickets_data1 = {
            '_json_att':'',
        }
        get_tickets_resp1 = mysession.request(
            method='POST',
            url=get_tickets_url1,
            headers=myheader,
            data=get_tickets_data1
        )
        get_tickets_res1 = json.loads(get_tickets_resp1.content.decode('utf8'))
        # print(get_tickets_res1)
        '''
        print(get_tickets_res1)
        {'validateMessagesShowId': '_validatorMessage', 'status': True, 'httpstatus': 200, 
        'data': {'flag': True}, 'messages': [], 'validateMessages': {}}
        '''

        # 第二次请求
        get_tickets_url2 = 'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest'
        for k,v in pot_choice_dic.items():
            mysecretstr = v[0]
            break
        get_tickets_data2 = {
            'secretStr':urllib.parse.unquote(mysecretstr),
            'train_date':'2019-02-03',
            'back_train_date':'2019-01-09',
            'tour_flag':'dc',
            'purpose_codes':'ADULT',
            'query_from_station_name':'昆明',
            'query_to_station_name':'玉溪',
            'undefined':'',
        }
        get_tickets_resp2 = mysession.request(
            method='POST',
            url=get_tickets_url2,
            headers=myheader,
            data=get_tickets_data2
        )
        get_tickets_res2 = json.loads(get_tickets_resp2.content.decode('utf8'))
        # print(get_tickets_res2)
        '''
        print(get_tickets_res2)
        {'validateMessagesShowId': '_validatorMessage', 
        'status': True, 'httpstatus': 200, 'data': 'N', 
        'messages': [], 'validateMessages': {}}
        '''

        # 第三次请求
        get_tickets_url3 = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'
        get_tickets_data3 = {
            '_json_att': '',
        }
        get_tickets_resp3 = mysession.request(
            method='POST',
            url=get_tickets_url3,
            headers=myheader,
            data=get_tickets_data3
        )
        get_tickets_res3 = get_tickets_resp3.content.decode('utf8')
        # 此处通过正则表达式获取后面两个请求需要发送的参数
        globalRepeatSubmitToken = re.findall(r"globalRepeatSubmitToken = '(.*?)';",get_tickets_res3)[0]
        key_check_isChange = re.findall(r"'key_check_isChange':'(.*?)',",get_tickets_res3)[0]
        leftTicketStr = re.findall(r"'leftTicketStr':'(.*?)',",get_tickets_res3)[0]
        # print(leftTicketStr)

        # 第四次请求
        get_tickets_url4 = 'https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs'
        get_tickets_data4 = {
            '_json_att': '',
            'REPEAT_SUBMIT_TOKEN':globalRepeatSubmitToken,
        }
        get_tickets_resp4 = mysession.request(
            method='POST',
            url=get_tickets_url4,
            headers=myheader,
            data=get_tickets_data4
        )
        get_tickets_res4 = json.loads(get_tickets_resp4.content.decode('utf8'))
        # print(get_tickets_res4)
        global guests_info_dic
        normal_passengers_li = get_tickets_res4['data']['normal_passengers']
        for i in normal_passengers_li:
            guests_info_dic[i['passenger_id_no']] = i
        # print(guests_info_dic)

        # 第五次请求:确认订单信息
        '''
        cancel_flag	2
        bed_level_order_num	000000000000000000000000000000
        passengerTicketStr	1,0,1,陆翠华,1,53011219540628032X,,N_1,0,1,张帆,1,532401198003090030,,N_1,0,1,张兴,1,530112198210080311,18687027119,N_1,0,1,张文恕,1,530112195310270311,,N
        oldPassengerStr	陆翠华,1,53011219540628032X,1_张帆,1,532401198003090030,1_张兴,1,530112198210080311,1_张文恕,1,530112195310270311,1_
        tour_flag	dc
        randCode	
        whatsSelect	1
        _json_att	
        REPEAT_SUBMIT_TOKEN	16eac430394acc1d6135ca0f1bdd1fae
        '''
        get_tickets_url5 = 'https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo'
        get_tickets_data5 = {
            'cancel_flag':'2',
            'bed_level_order_num':'000000000000000000000000000000',
            'passengerTicketStr':'1,0,1,张兴,1,530112198210080311,18687027119,N',
            'oldPassengerStr':'张兴,1,530112198210080311,1_',
            'tour_flag':'dc',
            'randCode':'',
            'whatsSelect':'1',
            '_json_att':'',
            'REPEAT_SUBMIT_TOKEN':globalRepeatSubmitToken
        }
        get_tickets_resp5 = mysession.request(
            method='POST',
            url=get_tickets_url5,
            headers=myheader,
            data=get_tickets_data5
        )
        get_tickets_res5 = json.loads(get_tickets_resp5.content.decode('utf8'))
        print('get_tickets_res5: ',get_tickets_res5)

        # 第六次请求:获取时时余票(一直无法获取，未找到原因)
        myheader6 = {
            'Referer': 'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
        }
        get_tickets_url6 = 'https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount'
        get_tickets_data6 = {
            'train_date':'Sun+Feb+03+2019+00:00:00+GMT+0800+(中国标准时间)',
            'train_no':'240000K63503',
            'stationTrainCode': 'K638',
            'seatType': '1',
            'fromStationTelecode': 'KMM',
            'toStationTelecode': 'AXM',
            'leftTicket': leftTicketStr,
            'purpose_codes': '00',
            'train_location': 'P4',
            '_json_att': '',
            'REPEAT_SUBMIT_TOKEN': globalRepeatSubmitToken,
        }
        get_tickets_resp6 = mysession.request(
            method='POST',
            url=get_tickets_url6,
            headers=myheader6,
            data=get_tickets_data6
        )
        get_tickets_res6 = json.loads(get_tickets_resp6.content.decode('utf8'))
        # get_tickets_res6 = get_tickets_resp6.content.decode('utf8')
        print('get_tickets_res6: ',get_tickets_res6)

        # 第七次请求:确认订单
        get_tickets_url7 = 'https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue'
        get_tickets_data7 = {
            'passengerTicketStr': '1,0,1,张兴,1,530112198210080311,18687027119,N',
            'oldPassengerStr':'张兴,1,530112198210080311,1_',
            'randCode':'',
            'purpose_codes':'00',
            'key_check_isChange':key_check_isChange,
            'leftTicketStr':leftTicketStr,
            'train_location':'P4',
            'choose_seats':'',
            'seatDetailType':'000',
            'whatsSelect':'1',
            'roomType':'0',
            'dwAll':'N',
            '_json_att':'',
            'REPEAT_SUBMIT_TOKEN':globalRepeatSubmitToken
        }
        get_tickets_resp7 = mysession.request(
            method='POST',
            url=get_tickets_url7,
            headers=myheader,
            data=get_tickets_data7
        )
        get_tickets_res7 = json.loads(get_tickets_resp7.content.decode('utf8'))
        # get_tickets_res7 = get_tickets_resp7.content.decode('utf8')
        print('get_tickets_res7: ',get_tickets_res7)

        # exit('调试中断')

        # 第八次请求:循环获取订单号
        orderId = ''
        while not orderId:
            myrandom = str(int(time.time() * 1000))
            get_tickets_url8 = 'https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime'
            get_tickets_params8 = {
                'random:':myrandom,
                'tourFlag':'dc',
                '_json_att':'',
                'REPEAT_SUBMIT_TOKEN':globalRepeatSubmitToken,
            }
            get_tickets_resp8 = mysession.request(
                method='GET',
                url=get_tickets_url8,
                headers=myheader,
                params=get_tickets_params8,
            )
            get_tickets_res8 = json.loads(get_tickets_resp8.content.decode('utf8'))
            # get_tickets_res8 = get_tickets_resp8.content.decode('utf8')
            # print('get_tickets_res8: ',get_tickets_res8)
            orderId = get_tickets_res8['data']['orderId']
            print(orderId)
            # 此处可以定义间隔多长时间请求一次订单号
            # time.sleep(1)

        # 第九次请求:下单
        get_tickets_url9 = 'https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForDcQueue'
        get_tickets_data9 = {
            'orderSequence_no':orderId,
            '_json_att':'',
            'REPEAT_SUBMIT_TOKEN':globalRepeatSubmitToken
        }
        get_tickets_resp9 = mysession.request(
            method='POST',
            url=get_tickets_url9,
            headers=myheader,
            data=get_tickets_data9
        )
        get_tickets_res9 = json.loads(get_tickets_resp9.content.decode('utf8'))
        # get_tickets_res9 = get_tickets_resp9.content.decode('utf8')
        print('get_tickets_res9: ',get_tickets_res9)

        # 第十次请求:确认下单
        get_tickets_urlx = 'https://kyfw.12306.cn/otn//payOrder/init'
        get_tickets_datax = {
            '_json_att':'',
            'REPEAT_SUBMIT_TOKEN':globalRepeatSubmitToken
        }
        myrandom2 = str(int(time.time() * 1000))
        get_tickets_paramsx = {
            'random:': myrandom2,
        }
        get_tickets_respx = mysession.request(
            method='POST',
            url=get_tickets_urlx,
            headers=myheader,
            data=get_tickets_datax,
            params=get_tickets_paramsx,
        )
        # get_tickets_resx = json.loads(get_tickets_respx.content.decode('utf8'))
        get_tickets_resx = get_tickets_respx.content.decode('utf8')
        # print('get_tickets_resx: ',get_tickets_resx)

    else: # 无票打印无票
        print('no ticket left!')
        return False



if __name__ == '__main__':
    # auth_user_account()
    while True:
        user_choice = input('input code(Y|N):').strip()
        if user_choice.upper() == 'Y':
            get_ticket()
        else:
            break