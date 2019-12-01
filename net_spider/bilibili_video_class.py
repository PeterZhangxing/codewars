import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json


class DownLoadVideo(object):
    '''
    https://www.bilibili.com/video/av53722175/
    aid=53722175&page=1&platform=html5&quality=1&vtype=mp4&type=jsonp
    '''

    def __init__(self,file_name,aid,browser="Chrome"):

        self.file_name = file_name + ".mp4"
        if hasattr(webdriver,browser):
            self.driver = getattr(webdriver,browser)()
        else:
            raise NameError("no such browser!")

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3521.2 Safari/537.36"
        }
        self.aid = aid
        self.bili_get_cookie_url = "https://www.bilibili.com/video/{}/".format("av"+aid)
        self.download_base_url = "https://api.bilibili.com/playurl"

        self.get_logged_cookie()


    def get_logged_cookie(self):

        self.driver.get(self.bili_get_cookie_url)

        time.sleep(10)
        # 获取当前页面的cookie
        cookies = self.driver.get_cookies()

        # 提取cookie的值为大字典的键值对类型，去掉不必要的字段

        self.cookies = {i["name"]: i["value"] for i in cookies}
        print(self.cookies)

        self.driver.quit()


    def save_file(self,video_file):

        if not os.path.exists("tmp/bilibili/"):
            os.mkdir("tmp/bilibili/")

        file_path = os.path.join("tmp/bilibili",self.file_name)
        while os.path.isfile(file_path):
            self.file_name = str(input("input new file name:").strip())
            file_path = os.path.join("tmp/bilibili", self.file_name+'.mp4')

        try:
            with open(file_path, "wb") as f:
                f.write(video_file)
        except Exception as e:
            exit(str(e))


    def get_download_url(self):
        '''
        从json数据中，获取下载视频的url地址
        :return:
        '''
        params = {
            "aid":self.aid,
            "page":1,
            "platform":"html5",
            "quality":1,
            "vtype":"mp4",
            "type":"jsonp"
        }

        # 获取包含视频下载地址的json
        video_file_info_str = requests.get(
            url=self.download_base_url,
            params=params,
            headers=self.headers,
            cookies=self.cookies,
        ).content.decode("utf-8")
        # print(video_file_info_str)
        # print(self.cookies)

        # 从字典中获取视频下载的url
        video_file_info_dic = json.loads(video_file_info_str)
        video_download_url = video_file_info_dic["durl"]["0"]["url"]
        print(video_download_url)

        return video_download_url


    def download_video(self):

        video_download_url = self.get_download_url()

        try:
            video_file = requests.get(
                url=video_download_url,
                headers=self.headers,
                cookies=self.cookies,
            ).content
        except Exception as e:
            exit(str(e))

        print("file_size : ",len(video_file))

        self.save_file(video_file)

        print("finished dowmload!")


if __name__ == '__main__':
    myvideo = DownLoadVideo("9m88","21807063")
    myvideo.download_video()