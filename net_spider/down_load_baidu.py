import requests
import os


"kw=lol&ie=utf-8&pn=100"
class TiebaSpider(object):

    def __init__(self,kw,end_page):
        self.kw = kw
        self.end_page = end_page
        self.url_base = "https://tieba.baidu.com/f"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3521.2 Safari/537.36"
        }
        self.buid_url_li()

    def buid_url_li(self):
        params_li = []
        for i in range(self.end_page):
            tmp_dict = {}
            tmp_dict["kw"] = self.kw
            tmp_dict["pn"] = i * 50
            tmp_dict["ie"] = "utf-8"
            params_li.append(tmp_dict)
        self.params_li = params_li

    def save_html_file(self,page_num,content):
        file_path = os.path.join('tmp',self.kw,self.kw+str(page_num)+".html")
        if not os.path.exists(os.path.join('tmp',self.kw)):
            os.mkdir(os.path.join('tmp',self.kw))
        with open(file_path,"wb") as f:
            f.write(content)

    def down_load(self):
        i = 1
        for params in self.params_li:
            resp = requests.get(
                url=self.url_base,
                params=params,
                headers=self.headers,
            )
            self.save_html_file(i,resp.content)
            i += 1


if __name__ == '__main__':
    myspider = TiebaSpider("lol",3)
    myspider.down_load()