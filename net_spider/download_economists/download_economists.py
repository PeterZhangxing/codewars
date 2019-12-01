# 下载指定的那期经济学人

import re,datetime,requests,os,sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from download_economists import settings


class DownLoadEco(object):

    def __init__(self):
        self.url = settings.url_model

        # 正则表达式测试
        # res1 = re.findall(r"\d{4}-\d{2}-\d{2}",url)
        # res2 = re.search(r"\d{4}-\d{2}-\d{2}",url).group()
        # res3 = re.match(r"\d{4}-\d{2}-\d{2}",url)
        # print(res1) # ['2018-11-24', '2018-11-24']
        # print(res2) # 2018-11-24
        # print(res3) # None

        # 分别获取当前时间的年月日
        self.current_date_dict = {"tm_year": "", "tm_mon": "", "tm_mday": ""}
        for k, v in self.current_date_dict.items():
            if hasattr(datetime.date.timetuple(datetime.datetime.now()), k):
                self.current_date_dict[k] = str(getattr(datetime.date.timetuple(datetime.datetime.now()), k))
        # print(self.current_date_dict)

        # 创建下载文件的url,和文件名称
        self.create_url_filename()


    def check_date_num(self,num_str):
        '''
        检测输入的字符是不是数字
        :param num_str:
        :return:
        '''
        if num_str.isdigit():
            return True
        else:
            return False


    def create_url_filename(self):
        '''
        根据输入信息，创建文件名和下载文件的url地址
        :return:
        '''
        while True:
            year = input(
                "Please input the year in which the magazine had been published(default %s): "%self.current_date_dict["tm_year"]
            ).strip()\
                   or self.current_date_dict["tm_year"]
            if self.check_date_num(year):
                break
            else:
                print("Invalid year")

        while True:
            month = input(
                "Please input the month in which the magazine had been published(default %s): "%self.current_date_dict["tm_mon"]
            ).strip()\
                    or self.current_date_dict["tm_mon"]
            if self.check_date_num(month):
                break
            else:
                print("Invalid month")

        while True:
            day = input(
                "Please input the day on which the magazine had been published(default %s): "%self.current_date_dict["tm_mday"]
                        ).strip()\
                  or self.current_date_dict["tm_mday"]
            if self.check_date_num(day):
                break
            else:
                print("Invalid day")

        self.new_url = re.sub(r"\d{4}-\d{2}-\d{2}","%s-%s-%s"%(year,month,day),self.url)
        print("Prepare to download magazine from %s"%self.new_url)

        self.filename = self.new_url.split('/')[-2]


    def file_name_check(self):
        '''
        检查文件是不是已经存在于下载目录
        :return:
        '''
        if os.path.exists(os.path.join(self.download_dir, self.filename)):
            return True
        else:
            return False


    def prepare_download_magazine(self):
        '''
        准备好下载目录，并处理文件重名的问题
        :return:
        '''
        self.download_dir = os.path.join(settings.BASE_DIR,"download_files")

        if not os.path.isdir(self.download_dir):
            os.mkdir(self.download_dir)

        while self.file_name_check():
            choice = input(
                "%s had been downloaded before,\n if you want to download it again,\n please type 'y',\n type 'n' to abort downloading,\n type 'r' to rename the file: "%self.filename
            ).strip().lower()

            if choice and choice == 'y':
                return True
            elif choice and choice == 'n':
                return False
            elif choice and choice == 'r':
                self.filename = input("Input the new file_name here: ").strip()
                # self.prepare_download_magazine()
                # return self.file_name_check()
            else:
                pass

        return True


    def download_magazine(self):
        '''
        下载文件，并保持到指定的目录中
        :return:
        '''
        try:
            if not self.prepare_download_magazine():
                exit("Quit downloading!")

            # 开始下载文件
            print("start downloading %s"%self.filename)
            respons = requests.get(
                url=self.new_url,
                stream=True,
            )

            # 用文件大小判断杂志是否存在
            respons_len = len(respons.content)//(1024*1024)
            if respons_len < 5:
                raise Exception(
                    "No such magazine named %s,please try run this programme again."%self.filename)

            # 将文件存储到本地
            with open(os.path.join(self.download_dir, self.filename), 'wb') as f:
                f.write(respons.content)

        except Exception as e:
            exit(str(e))
        else:
            print("finished downloading %s(%s MB)"%(self.filename,respons_len))


if __name__ == '__main__':

    my_downloader = DownLoadEco()
    my_downloader.download_magazine()
