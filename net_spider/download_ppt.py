import re
import os

def change_file_name(string):
    # string = "b931c32feefdc8d376ee322b (1).jpg"
    # pic_str = string.rsplit(" ",1)[1]
    # print(num) # (1).jpg

    pat = re.compile(r'^\w+\s+\((\d+)\).*')

    try:
        num = pat.findall(string)[0]
        # print(num,type(num))

        file_name = "python交流"+num+".jpg"

        # print(file_name) # python交流1.jpg
        return file_name
    except Exception as e:
        return None

base_dir = os.getcwd()
file_li = os.listdir(base_dir)

for file in file_li:
    full_file_ori_name = os.path.join(base_dir,file)

    changed_name = change_file_name(file)
    if not changed_name:
        continue

    full_file_dst_name = os.path.join(base_dir,changed_name)
    os.rename(full_file_ori_name,full_file_dst_name)