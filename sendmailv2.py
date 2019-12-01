import smtplib,os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

def mySendMail(subject,receiver,fimage_name, ffile_name,inputtext=None,sendimagefile=None,sendfile=None,sender='99360681@qq.com'):
    try:
        # 生成整个邮件体对象，再后面可以为其添加文本，html，图片，文件等内容发送过去
        msg = MIMEMultipart('mixed')
        msg['Subject'] = subject
        msg['From'] = '%s <%s>' % (sender, sender)
        msg['To'] = ";".join(receiver)

        # 生成普通文本内容，并添加到mixed对象
        if inputtext != None:
            text = str(inputtext)
            text_plain = MIMEText(text, 'plain', 'utf-8')
            msg.attach(text_plain)

        if sendimagefile != None:
            # 生成图片内容，，并添加到mixed对象
            image = MIMEImage(sendimagefile)
            image.add_header('Content-ID', '<image1>')
            image["Content-Disposition"] = 'attachment; filename="%s"'%(fimage_name)
            msg.attach(image)

        if sendfile != None:
            # 生成普通文件内容，，并添加到mixed对象
            text_att = MIMEText(sendfile, 'base64', 'utf-8')
            text_att["Content-Type"] = 'application/octet-stream'
            text_att.add_header('Content-Disposition', 'attachment', filename='%s'%(ffile_name))
            msg.attach(text_att)

    except Exception as e:
        print(str(e))
    else:
        send_my_mail(sender,receiver,msg)


def send_my_mail(sender,receiver,msg,smtpserver='smtp.qq.com',username='99360681@qq.com',password='cdbnlajjhfctbjhb'):
    # 用于建立和邮件发送服务器的连接，并发送邮件
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
    except Exception as e:
        print(str(e))
    else:
        print('Mail to %s have been send successfully.'%(receiver))


def get_file_name(input_fimage_path=None, input_ffile_path=None):
    # 对作为附件的文件进行处理，并把结果返回
    if input_fimage_path == None:
        input_fimage_path = 'E:\Entertainment\photos\100_FUJI\DSCF0515.JPG'
    fimage_name = os.path.basename(input_fimage_path)
    fimage = open(input_fimage_path, 'rb')
    sendimagefile = fimage.read()
    fimage.close()

    if input_ffile_path == None:
        input_ffile_path = 'E:\PycharmProjects\codewars\get_ip.py'
    ffile_name = os.path.basename(input_ffile_path)
    ffile = open(input_ffile_path, 'rb')
    sendfile = ffile.read()
    ffile.close()

    # print(fimage_name, ffile_name,)

    return (fimage_name, ffile_name, sendimagefile, sendfile)


if __name__ == "__main__":
    subject = input('Input the title of your email here : ')
    inputtext = input("Input the content of your email here : ")

    fimage_name, ffile_name, sendimagefile, sendfile = get_file_name()

    recer = ['20643257@qq.com']

    mySendMail(subject,recer,fimage_name,ffile_name,inputtext,sendimagefile,sendfile)
