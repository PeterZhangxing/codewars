#!/usr/bin/python3.5

import requests,os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
statc_path = os.path.join(BASE_DIR,'statics')

# 获取返回报文的头部，响应码，页面内容
status_head = requests.get("http://www.dygang.net/").headers
return_code = requests.get("http://www.dygang.net/").status_code
http_body = requests.get("http://www.dygang.net/").text

# 把返回的页面保存到指定的文件中
with open(os.path.join(statc_path,'dygang.net.html'),'w',encoding='utf-8') as f:
    for line in http_body:
        f.write(line)

