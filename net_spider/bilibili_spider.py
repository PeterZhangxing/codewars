import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json


headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3521.2 Safari/537.36"
        }

bili_url = "https://www.bilibili.com/video/av53722175/"

download_url = "https://api.bilibili.com/playurl?aid=53722175&page=1&platform=html5&quality=1&vtype=mp4&type=jsonp"

driver = webdriver.Chrome()
# 发送get请求
driver.get(bili_url)

# 获取当前页面的cookie
cookies = driver.get_cookies()

# 提取cookie的值为大字典的键值对类型，去掉不必要的字段
time.sleep(6)
cookies = {i["name"]:i["value"] for i in cookies}
print(cookies)

driver.quit()

video_file_info_str = requests.get(
    url=download_url,
    headers=headers,
    cookies=cookies,
).content.decode("utf-8")

video_file_info_dic = json.loads(video_file_info_str)
video_download_url = video_file_info_dic["durl"]["0"]["url"]
print(video_download_url)

try:
    video_file = requests.get(
        url=video_download_url,
        headers=headers,
        cookies=cookies,
    ).content
except Exception as e:
    exit(str(e))

print(len(video_file))

with open("tmp/video1.mp4","wb") as f:
    f.write(video_file)

print("finished downloading!")