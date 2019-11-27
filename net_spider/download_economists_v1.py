# 下载指定的那期经济学人

import re,datetime,requests,os


url = "https://github.com/nailperry-zd/The-Economist/raw/master/2018-11-24/The_Economist_-_2018-11-24.mobi/"

# 正则表达式测试
# res1 = re.findall(r"\d{4}-\d{2}-\d{2}",url)
# res2 = re.search(r"\d{4}-\d{2}-\d{2}",url).group()
# res3 = re.match(r"\d{4}-\d{2}-\d{2}",url)
# print(res1) # ['2018-11-24', '2018-11-24']
# print(res2) # 2018-11-24
# print(res3) # None

def check_date_num(num_str):
    if num_str.isdigit():
        # print("hhhhhhhh")
        return True
    else:
        return False

current_date_dict = {"tm_year":"","tm_mon":"","tm_mday":""}

for k,v in current_date_dict.items():
    if hasattr(datetime.date.timetuple(datetime.datetime.now()),k):
        current_date_dict[k] = str(getattr(datetime.date.timetuple(datetime.datetime.now()),k))

# print(current_date_dict)

while True:
    year = input("Please input the year in which the magazine had been published(such as 2018): ").strip()\
           or current_date_dict["tm_year"]
    if check_date_num(year):
        break
    else:
        print("Invalid year")

while True:
    month = input("Please input the month in which the magazine had been published(such as 11): ").strip()\
            or current_date_dict["tm_mon"]
    if check_date_num(month):
        break
    else:
        print("Invalid month")

while True:
    day = input("Please input the day on which the magazine had been published(such as 28): ").strip()\
          or current_date_dict["tm_mday"]
    if check_date_num(day):
        break
    else:
        print("Invalid day")

while True:
    d_type = input("Please input the type of magazine(such as pdf): ").strip()\
          or "mobi"
    if d_type in ["mobi","pdf"]:
        break
    else:
        print("Invalid document type")

new_url = re.sub(r"\d{4}-\d{2}-\d{2}","%s-%s-%s"%(year,month,day),url)
new_url = re.sub(r"mobi",d_type,url)

print(new_url)

filename = new_url.split('/')[-2]
print(filename)

try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    download_dir = os.path.join(BASE_DIR,"download_files")

    if os.path.exists(os.path.join(download_dir,filename)):
        while True:
            choice = input(
                "%s had been downloaded before,if you want to download it again ,please type 'y',else 'n' to abort: "%filename
                           ).strip().lower()
            if choice and choice == 'y':
                    break
            elif choice and choice == 'n':
                exit('Quit downloading!')
                # filename = input("Please input a new name for %s"%filename).strip()
            else:
                pass

    # 开始下载文件
    print("start downloading %s"%filename)
    respons = requests.get(
        url=new_url,
        stream=True,
    )
    # 用文件大小判断杂志是否存在
    respons_len = len(respons.content)//(1024*1024)
    if respons_len < 5:
        raise Exception("No such magazine named %s,please try run this programme again."%filename)
    # 将文件存储到本地
    with open(os.path.join(download_dir, filename), 'wb') as f:
        f.write(respons.content)

except Exception as e:
    exit(str(e))
else:
    print("finished downloading %s(%s MB)"%(filename,respons_len))