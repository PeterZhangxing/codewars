import ftplib
import time

hostname = 'ftp.hh010.com'
port = 21

username ='honghu2426'
password = 'Zhangxing20_05@'

# ftp_encode=['UTF-8','gbk','GB2312','GB18030','Big5','HZ']

def show_simple_chinese(string):
    '''
    正常显示中文
    :param string:
    :return:
    '''
    res = string.encode('iso-8859-1').decode('gbk')
    return res

def transform_name(string):
    '''
    将中文转换为ftp识别的字符
    :param string:
    :return:
    '''
    item = string.encode('gbk').decode('iso-8859-1')
    return item

def get_bfile(ftpobj,filename):
    '''
    从ftp站点，以二进制方式下载文件
    :param ftpobj:
    :param filename:
    :return:
    '''
    f = open(show_simple_chinese(filename), 'wb')  # 打开要保存文件
    newfilename = 'RETR ' + filename  # 保存FTP文件
    ftpobj.retrbinary(newfilename, f.write)
    f.close()
    print('already download %s'%show_simple_chinese(filename))

def send_bfile(ftpobj,filename):
    '''
    以二进制方式，上传文件到ftp站点
    :param ftpobj:
    :param filename:
    :return:
    '''
    try:
        newfilename = 'STOR ' + filename
        upload_file = open(show_simple_chinese(filename), 'rb')
        ftpobj.storbinary(newfilename, upload_file)
        print('%s uploaded to ftp server'%show_simple_chinese(filename))
    except Exception as e:
        print(str(e))

def del_ftp_file(ftpobj,filename):
    '''
    删除发ftp上的指定文件
    :param ftpobj:
    :param filename:
    :return:
    '''
    try:
        ftpobj.delete(filename)
        print('already deleted %s'%show_simple_chinese(filename))
    except Exception as e:
        print(str(e))

ftpobj = ftplib.FTP()
try:
    ftpobj.connect(host=hostname,port=port,timeout=30)
    ftpobj.login(user=username,passwd=password)
    # ftpobj.encoding = 'GB2312'

    wel_info = ftpobj.getwelcome()
    print(show_simple_chinese(wel_info))

    dir_li = ftpobj.nlst()
    print([ show_simple_chinese(item) for item in dir_li ])

    print(ftpobj.pwd())
    ftpobj.cwd(transform_name('编程/明星Python教程/04-《明星Python教程》Python语言编程基础'))
    dir_li = ftpobj.nlst()
    print([show_simple_chinese(item) for item in dir_li])
    print(show_simple_chinese(ftpobj.pwd()))

    # get_bfile(ftpobj,transform_name('鸿鹄论坛_5.1输入输出格式IoConsole.rar'))

    time.sleep(3)

    # send_bfile(ftpobj,transform_name('阅读器.rar'))

    del_ftp_file(ftpobj,transform_name('鸿鹄论坛_5.1输入输出格式IoConsole.rar'))

    ftpobj.quit()
except Exception as e:
    print(str(e))