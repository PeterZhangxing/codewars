#/usr/bin/python3.5

import urllib.request
from bs4 import BeautifulSoup
import os,re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
htmlfile = os.path.join(BASE_DIR,"statics","test.html")
# print(htmlfile)

with open(htmlfile,'r',encoding='utf-8') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc,"html.parser")
docks = soup.prettify(formatter="html")
mkds = BeautifulSoup(docks,"html.parser")

for x in mkds.find_all(id="content"):
    string = x.get_text()
    string.replace(u'\xa0',u' ')
    with open(os.path.join(BASE_DIR,"statics","h.txt"),"a+") as f:
        f.write(string)