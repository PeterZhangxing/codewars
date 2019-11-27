#!/usr/bin/python3.7

from twilio.rest import Client

class My_Twilio_SMS(object):

    def __init__(self,account="AC22996c1be830bb199cebfab68e7ed03f",token="3ea2e0e84ae9efc2a222bf1984086d61"):
        '''
        # twilio分配的账号ID
        account = "AC22996c1be830bb199cebfab68e7ed03f"
        # twilio分配的安全密钥
        token = "3ea2e0e84ae9efc2a222bf1984086d61"
        '''
        # 实例化发送短信的客户端对象
        try:
            self.client = Client(account,token)
        except Exception as e:
            exit(str(e))

    def my_send_SMS(self,message_body,sender_num,receiver_num):
        '''
        发送短信
        :param message_body:
        :param sender_num:
        :param receiver_num:
        :return:
        '''
        try:
            self.client.messages.create(to=receiver_num,from_=sender_num,body=message_body)
        except Exception as e:
            exit(str(e))
        else:
            print("message to %s has successfully sended!"%receiver_num)


if __name__ == '__main__':

    # 短信内容
    message_body = "This is a SMS from zhangxing!"

    # twilio分配的发送短信用的号码
    sender_num = "+14693457649"

    # 接收短信的用户号码
    # receiver_num_list = ["+8618687001736", "+8618687027119", "+8613529209726","+8618552064396"]
    receiver_num_list = ["+8618552064396"]

    # 创建并发送短信
    # message = client.messages.create(to=receiver_num,from_=sender_num,body=message_body)
    mysms = My_Twilio_SMS()
    for receiver_num in receiver_num_list:
        mysms.my_send_SMS(message_body,sender_num,receiver_num)
