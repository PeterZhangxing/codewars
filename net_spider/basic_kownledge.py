import requests
from bs4 import BeautifulSoup


# 通过代理发送post请求到目的url，相当于换了http请求的源地址
# post_dict = {
#     "phone": '8615131255089',
#     'password': 'woshiniba',
#     'oneMonth': 1
# }
# response = requests.post(
#     url="http://dig.chouti.com/login",
#     data=post_dict,
#     proxys={ # 指明代理服务器的地址
#         'http': "http://4.19.128.5:8099"
#     }
# )


# 使用post方式，上传文件对象
# requests.post(
#     url='xxx',
#     files={
#         'f1': open('s1.py','rb'),
#         'f2': ('ssssss1.py',open('s1.py','rb'))
#     }
# )


# 向网页发起加密的ssl访问
# requests.get(
#     url='https:xxxx',
    # verify=False # 指明是否需要验证证书的有效性
    # cert='fuck.pem' # 指明CA发给被访问网站的证书
    # cert=('fuck.crt','xxx.key') # 指明CA发给被访问网站的证书
# )


# 下载指定的那期经济学人
# import re,datetime

# url = "https://github.com/nailperry-zd/The-Economist/raw/master/2018-11-24/The_Economist_-_2018-11-24.mobi/"

# 正则表达式测试
# res1 = re.findall(r"\d{4}-\d{2}-\d{2}",url)
# res2 = re.search(r"\d{4}-\d{2}-\d{2}",url).group()
# res3 = re.match(r"\d{4}-\d{2}-\d{2}",url)
# print(res1) # ['2018-11-24', '2018-11-24']
# print(res2) # 2018-11-24
# print(res3) # None

# current_date_dict = {"tm_year":"","tm_mon":"","tm_mday":""}
#
# for k,v in current_date_dict.items():
#     if hasattr(datetime.date.timetuple(datetime.datetime.now()),k):
#         current_date_dict[k] = str(getattr(datetime.date.timetuple(datetime.datetime.now()),k))
#
# print(current_date_dict)
#
# year = input("Please input the year in which the magazine had been published(such as 2018): ").strip()\
#        or current_date_dict["tm_year"]
# month = input("Please input the month in which the magazine had been published(such as 11): ").strip()\
#         or current_date_dict["tm_year"]
# day = input("Please input the day on which the magazine had been published(such as 28): ").strip()\
#       or current_date_dict["tm_mday"]
#
# new_url = re.sub(r"\d{4}-\d{2}-\d{2}","%s-%s-%s"%(year,month,day),url)
#
# print(new_url)

# filename = url.split('/')[-1]
#
# try:
#     respons = requests.get(
#         url=url,
#     )
#     with open(filename,'wb') as f:
#         f.write(respons.content)
# except Exception as e:
#     exit(str(e))
# else:
#     print("finished downloading %s"%filename)


# 通过在网页上搜索，下载某个网页上指定的内容
# response = requests.get(
#     url='http://www.autohome.com.cn/news/'
# )

# response.encoding = response.apparent_encoding # 指定文本的编码方式，为响应报文中的编码方式
# soup = BeautifulSoup(response.text,features='html.parser') # 格式化html文本，输出为对象，每一个标签都变成对象
# target = soup.find(id='auto-channel-lazyload-article') # 在当前对象中找到所有的指定id的标签对象
# li_list = target.find_all('li') # 在当前对象中找到所有的li标签，返回的是对象的列表
# for i in li_list:
#     a = i.find('a')
#     if a:
#         print(a.attrs.get('href'))
#         txt = a.find('h3').text # 获取某个标签对象的文本内容
#         print(txt)
#         img_url = a.find('img').attrs.get('src') # 获取某个标签对象的某个属性的值
#         print(img_url)
#
#         # 保存文件到本地指定目录
#         img_response = requests.get(url=img_url)
#         import uuid
#         file_name = str(uuid.uuid4()) + '.jpg'
#         with open(file_name,'wb') as f:
#             f.write(img_response.content)