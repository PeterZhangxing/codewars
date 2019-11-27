#!/usr/bin/python3.5

import smtplib,os,poplib,email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
import os,time


############## 发送邮件的代码 #############

class My_Email_Send(object):

    def __init__(self,subject, receiver,inputtext=None, sender='99360681@qq.com',
                 smtpserver='smtp.qq.com', username='99360681@qq.com',password='cdbnlajjhfctbjhb',
                 input_fimage_path=None, input_ffile_path=None,with_attachments=False,*args,**kwargs):
        '''
        初始化发送邮件使用的对象
        '''
        # 构建邮件头部的参数
        self.subject = subject
        self.receiver = receiver
        self.inputtext = inputtext
        self.sender = sender

        # 构建连接发送邮件服务器的参数
        self.smtpserver = smtpserver
        self.username = username
        self.password = password

        # 构建作为附件的文件的参数
        self.input_fimage_path = input_fimage_path
        self.input_ffile_path = input_ffile_path
        if with_attachments:
            self.fimage_name, self.ffile_name, self.sendimagefile, self.sendfile = self.get_file_name()
        else:
            self.fimage_name = None
            self.ffile_name = None
            self.sendimagefile = None
            self.sendfile = None


    def get_file_name(self):
        '''
        对作为附件的文件进行处理，并把结果返回
        :return:
        '''
        if not self.input_fimage_path:
            self.input_fimage_path = 'E:\Entertainment\photos\100_FUJI\DSCF0515.JPG'
        fimage_name = os.path.basename(self.input_fimage_path)
        fimage = open(self.input_fimage_path, 'rb')
        sendimagefile = fimage.read()
        fimage.close()

        if not self.input_ffile_path:
            self.input_ffile_path = 'E:\PycharmProjects\codewars\get_ip.py'
        ffile_name = os.path.basename(self.input_ffile_path)
        ffile = open(self.input_ffile_path, 'rb')
        sendfile = ffile.read()
        ffile.close()

        return (fimage_name, ffile_name, sendimagefile, sendfile)


    def construct_email(self):
        '''
        构建邮件对象，添加文本和附件等内容，最后发送
        :return:
        '''
        try:
            # 生成整个邮件体对象，再后面可以为其添加文本，html，图片，文件等内容发送过去
            msg = MIMEMultipart('mixed')
            msg['Subject'] = self.subject
            msg['From'] = '%s <%s>' % (self.sender, self.sender)
            msg['To'] = ";".join(self.receiver)

            # 生成普通文本内容，并添加到mixed对象
            if self.inputtext != None:
                text = str(self.inputtext).strip()
                text_plain = MIMEText(text, 'plain', 'utf-8')
                msg.attach(text_plain)

            if self.sendimagefile != None:
                # 生成图片内容，，并添加到mixed对象
                image = MIMEImage(self.sendimagefile)
                image.add_header('Content-ID', '<image1>')
                image["Content-Disposition"] = 'attachment; filename="%s"' % (self.fimage_name)
                msg.attach(image)

            if self.sendfile != None:
                # 生成普通文件内容，，并添加到mixed对象
                text_att = MIMEText(self.sendfile, 'base64', 'utf-8')
                text_att["Content-Type"] = 'application/octet-stream'
                text_att.add_header('Content-Disposition', 'attachment', filename='%s' % (self.ffile_name))
                msg.attach(text_att)

        except Exception as e:
            exit(str(e))
        else:
            # 返回完整的邮件对象
            return msg
            # self.conn_mail(msg)


    def conn_mail(self,msg):
        # 用于建立和邮件发送服务器的连接，并发送邮件
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtpserver)
            smtp.login(self.username, self.password)
            smtp.sendmail(self.sender, self.receiver, msg.as_string())
            smtp.quit()
        except Exception as e:
            exit(str(e))
        else:
            print('Mail to %s have been send successfully.' % (self.receiver))


############## 接收邮件的代码 #############

# ADDR = '964725349@qq.com'
# PASSWORD = '****************'
# POP_SERVER = 'pop.qq.com'

class My_Email_Rec(object):

    def __init__(self, pop_server='pop.qq.com', user='964725349@qq.com',
                 passwd='kxsxacdjdelsbejc', *args,**kwargs):
        '''
        初始化接收邮件，获取第一封邮件标题字符的对象
        '''
        self.pop_server = pop_server
        self.user = user
        self.password = passwd


    def pop_connect(self):
        '''
        连接pop服务器，收取邮件
        :param self:
        :return:
        '''
        try:
           self.reademail = poplib.POP3_SSL(self.pop_server)
           self.reademail.user(self.user)
           self.reademail.pass_(self.password)
           self.allemail = self.reademail.stat()
        except Exception as e:
            exit('读取邮件登录失败::%s'%(str(e)))


    def receive_email(self):
        '''
        取得指定邮箱中，最新一封邮件的标题的字符串
        :return:
        '''
        # 连接邮箱，并获取所有邮件信息
        self.pop_connect()

        # 取得邮箱中第一封邮件的内容
        topemail = self.reademail.top(self.allemail[0], 0)

        # 编码邮件内容，格式化邮件，获取邮件头中的邮件标题
        emaillist = []
        for item in topemail[1]:
            try:
                emaillist.append(item.decode('utf8'))
            except:
                try:
                    emaillist.append(item.decode('gbk'))
                except:
                    emaillist.append(item.decode('big5'))
        # 格式化后的整个邮件的内容
        emailmsg = email.message_from_string('\n'.join(emaillist))
        emailsub = email.header.decode_header(emailmsg['subject'])
        # [(b'Weekly Coding Challenges\xc2\xa0', 'utf-8')]

        # 如果标题部分内容有存储有编码格式，则使用指定的格式编码进行解码，否则不解码
        if emailsub[0][1]:
            # [(b'Weekly Coding Challenges\xc2\xa0', 'utf-8')]
            submsg = emailsub[0][0].decode(emailsub[0][1])
        else:
            submsg = emailsub[0][0]

        # 返回第一封邮件的标题
        return submsg


############## 关机的代码 #############

class run_shutdown(object):

    def check_mail(self,my_recv_mail):
        res = my_recv_mail.receive_email()
        try:
            if res == "shutdown":
                os.system("shutdown -h 10")
                return "shutdown in 10 minutes"
            elif res == "shutdown now":
                os.system("shutdown -h now")
                return "shutdown right now"
            elif res == "reboot":
                os.system("shutdown -r 10")
                return "reboot in 10 minutes"
            elif res == "reboot now":
                os.system("shutdown -r now")
                return "reboot right now"
            else:
                return res
        except Exception as e:
            return str(e)


if __name__ == "__main__":

    ############################ 构建邮件内容标题和附件并发送 ############################

    # 构建邮件对象
    subject = input('Input the title of your email here : ')
    inputtext = input("Input the content of your email here : ")
    receiver = ['20643257@qq.com','964725349@qq.com']
    my_send_mail = My_Email_Send(subject,receiver,inputtext)

    # 发送邮件
    my_mail = my_send_mail.construct_email()
    my_send_mail.conn_mail(my_mail)
    

    ############################ 收取指定邮箱的邮件 ############################

    my_recv_mail = My_Email_Rec()
    res = my_recv_mail.receive_email()
    print(res)

    # ############################ 监控是不是收到邮件 ############################
    #
    # mycomputer = run_shutdown()
    # while True:
    #     res = mycomputer.check_mail(my_recv_mail)
    #     if res == "quit":
    #         exit("stop listening")
    #     time.sleep(60)
