import requests
from lxml import etree,html
import threading
from queue import Queue
import json
from bs4 import BeautifulSoup


class MulQiuBaiSpider(object):

    def __init__(self,page_num=None):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3521.2 Safari/537.36"
        }
        self.base_url = "https://www.qiushibaike.com/text/page/{}/"
        self.page_num =  page_num if page_num else self.get_total_page_num()
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()


    def build_url(self):
        for i in range(1,self.page_num+1):
            self.url_queue.put(self.base_url.format(i))


    def get_total_page_num(self):
        '''
        计算总共有多少个页面
        :return:
        '''
        total_page_num = 1
        while True:
            html_str = requests.get(
                self.base_url.format(total_page_num),
                headers=self.headers,
            ).content.decode("utf-8")
            # formated_html = etree.HTML(html_str)
            # next_page = formated_html.xpath("//ul[@class='pagination']//span[@class='next']/text()")

            bs = BeautifulSoup(html_str,"html.parser")
            page_ul = bs.find(name="ul",attrs={'class':'pagination'})
            next_page = page_ul.find(name="span",attrs={'class':'next'})
            # print(next_page)

            if next_page:
                total_page_num += 1
            else:
                return total_page_num


    def parse_url(self):
        while True:
            url = self.url_queue.get()
            resp = requests.get(
                url=url,
                headers=self.headers
            )
            self.html_queue.put(resp.content.decode("utf-8"))
            # 记录队列中还有多少数据的计数器减1，当计数器为0时，队列任务结束
            self.url_queue.task_done()


    def get_content_list(self):
        while True:
            # 获取并格式化单个页面
            html_str = self.html_queue.get()
            formated_html = etree.HTML(html_str)

            # 解析页面内容，获取所需数据，保存
            div_list = formated_html.xpath("//div[@id='content-left']/div")
            content_list = []

            for div in div_list:
                # item = {}
                # item["content"] = div.xpath(".//div[@class='content']/span/text()")
                # item["content"] = "   ".join([i.replace("\n", "") for i in item["content"]])
                # item["author_gender"] = div.xpath(".//div[contains(@class,'articleGender')]/@class")
                # item["author_gender"] = item["author_gender"][0].split(" ")[-1].replace("Icon", "") if len(item["author_gender"]) > 0 else None
                # item["auhtor_age"] = div.xpath(".//div[contains(@class,'articleGender')]/text()")
                # item["auhtor_age"] = item["auhtor_age"][0] if len(item["auhtor_age"]) > 0 else None
                # item["content_img"] = div.xpath(".//div[@class='thumb']/a/img/@src")
                # item["content_img"] = "https:" + item["content_img"][0] if len(item["content_img"]) > 0 else None
                # item["author_img"] = div.xpath(".//div[@class='author clearfix']//img/@src")
                # item["author_img"] = "https:" + item["author_img"][0] if len(item["author_img"]) > 0 else None
                # item["stats_vote"] = div.xpath(".//span[@class='stats-vote']/i/text()")
                # item["stats_vote"] = item["stats_vote"][0] if len(item["stats_vote"]) > 0 else None

                item = div.xpath(".//div[@class='content']/span/text()")
                item_li = [i.replace("\n", "") for i in item]
                content_list.append(item_li)

            self.content_queue.put(content_list)
            self.html_queue.task_done()


    def save_content_list(self):
        while True:
            content_list = self.content_queue.get()
            with open("qiushibai.txt","a",encoding="utf-8") as f:
                for content in content_list:
                    for p in content:
                        f.write(json.dumps(p,ensure_ascii=False))
                        f.write("\n")
                    f.write("\n\n")
            self.content_queue.task_done()


    def run(self):
        thread_list = []

        t_url = threading.Thread(target=self.build_url)
        thread_list.append(t_url)

        for i in range(2):
            t_parse = threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)

        t_html = threading.Thread(target=self.get_content_list)
        thread_list.append(t_html)

        t_save = threading.Thread(target=self.save_content_list)
        thread_list.append(t_save)

        for t in thread_list:
            t.setDaemon(True) #把子线程设置为守护线程，该线程不重要主线程结束，子线程结束
            t.start()

        for q in [self.url_queue,self.html_queue,self.content_queue]:
            q.join() #让主线程等待阻塞，等待队列的任务完成之后再完成

        print("main thread finished")



if __name__ == '__main__':
    myobj = MulQiuBaiSpider()
    # myobj.get_total_page_num()
    # print(myobj.page_num)
    myobj.run()