import requests
import json
import os


class DouMSpider(object):
    '''
    sort=S&range=0,10&tags=&start=0
    sort=S&range=0,10&tags=&start=20
    sort=S&range=0,10&tags=&start=40
    '''

    def __init__(self,nums=None):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3521.2 Safari/537.36"
        }
        self.base_url = "https://movie.douban.com/j/new_search_subjects"
        self.nums = nums


    def parse_data(self,start_num):
        params = {
            "sort":"S",
            "range":"0,10",
            "tags":"",
            "start":start_num
        }
        res = requests.get(
            url=self.base_url,
            headers=self.headers,
            params=params
        )
        return res.content.decode("utf-8")


    def json_data(self,str_data):
        tmp_dict = json.loads(str_data)
        data_li_size = len(tmp_dict["data"])
        return tmp_dict,data_li_size


    def save_data(self,tmp_dict):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        download_dir = os.path.join(BASE_DIR, "tmp","douban_download")
        if not os.path.isdir(download_dir):
            os.mkdir(download_dir)

        with open(os.path.join(download_dir,'douban.txt'),'a',encoding='utf-8') as f:
            for m_data in tmp_dict["data"]:
                data_dict = {}
                data_dict["movie_name"] = m_data["title"]
                data_dict["movie_rate"] = m_data["rate"]
                data_dict["movie_star"] = m_data["star"]
                json.dump(data_dict,f,ensure_ascii=False)
                f.write("\n")


    def run(self):
        num = 0
        while True:
            json_str = self.parse_data(num)
            tmp_dict, data_li_size = self.json_data(json_str)
            # print(data_li_size)

            self.save_data(tmp_dict)
            if self.nums == None:
                if data_li_size < 20:
                    break
                else:
                    num += 20
            elif self.nums * 20 > num:
                num += 20
            else:
                break



if __name__ == '__main__':
    mydouban = DouMSpider(10)
    mydouban.run()