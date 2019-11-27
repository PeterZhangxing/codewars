import requests
from bs4 import BeautifulSoup
import os,sys


# 1、通过下标标签获取一共有多少个页面
# 2、循环获取每个页面上的所有文章

#<ul class="list_14 p1_2 clearfix">
#   <li>
#       <a href="article/30431100" target="_blank">习近平讲故事：一株草，18年，两国情</a>[2018-11-29]
#   </li>
#</ul>

####### 页面下标代码 #######

# <div class="pagination pagination-centered">
#     <ul>
#         <li class="active">1</li>
#         <li><a href="http://jhsjk.people.cn/result/2" data-ci-pagination-page="2">2</a></li>
#         <li><a href="http://jhsjk.people.cn/result/3" data-ci-pagination-page="3">3</a></li>
#         <li><a href="http://jhsjk.people.cn/result/2" data-ci-pagination-page="2" rel="next">&gt;</a></li>
#         <a href="http://jhsjk.people.cn/result/46" data-ci-pagination-page="46">尾页</a>
#     </ul>
# </div>

class DownLoadArticle(object):

    def __init__(self,index_url):
        '''
        初始化下载类，创建下载目录，获取总页数
        :param index_url:
        '''
        self.index_url = index_url
        self.request_get_index_page()
        self.total_page_num = self.get_pagenum()
        self.download_dir = self.mk_downLoad_dir()


    def mk_downLoad_dir(self):
        '''
        保证保存下载文件的根文件夹存在
        :return:
        '''
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        download_dir = os.path.join(BASE_DIR, "download_files")
        if not os.path.isdir(download_dir):
            os.mkdir(download_dir)
        return download_dir


    def get_pagenum(self):
        '''
        获取目录的总页数
        :return:
        '''
        pagination = self.soup.find(name="div", attrs={"class": "pagination pagination-centered"})
        total_page_num = int(pagination.find(name="a", text="尾页").attrs.get("data-ci-pagination-page"))
        return total_page_num


    def request_get_index_page(self,c_page_num="1"):
        '''
        下载指定页码的目录页面，并格式化
        :param c_page_num:
        :return:
        '''
        try:
            self.response = requests.get(
                url=self.index_url + c_page_num,
            )
            self.response.encoding = self.response.apparent_encoding
            self.soup = BeautifulSoup(self.response.text, features='html.parser')
        except Exception as e:
            exit(str(e))


    def get_cur_index_dic(self,c_page_num):
        '''
        生成存储当前目录页面上，文章名称和文章地址的字典
        :param c_page_num:
        :return:
        '''
        self.request_get_index_page(c_page_num)
        cur_page_article_li = self.soup.find(name="ul", attrs={"class": "list_14 p1_2 clearfix"})
        li_objs = cur_page_article_li.find_all("li")
        artcle_dic_cur_page = {}
        for li_obj in li_objs:
            a_href = "http://jhsjk.people.cn/%s" % li_obj.find("a").attrs.get('href')
            a_txt = li_obj.text.strip()
            artcle_dic_cur_page[a_txt] = a_href
        return artcle_dic_cur_page


    def darticles_one_index(self,c_page_num):
        '''
        下载指定目录页面上的所有文章，到本地的子目录
        :param c_page_num:
        :return:
        '''
        artcle_dic_cur_page = self.get_cur_index_dic(c_page_num)
        for k, v in artcle_dic_cur_page.items():
            article_obj = requests.get(
                url=v,
            )

            self.sub_file_download_dir = os.path.join(self.download_dir,c_page_num)
            if not os.path.isdir(self.sub_file_download_dir):
                os.mkdir(self.sub_file_download_dir)

            file_name = str(k) + '.html'
            full_file_path = os.path.join(self.sub_file_download_dir,file_name)
            with open(full_file_path, 'wb') as f:
                f.write(article_obj.content)


def start_download(myarticle):
    # 获取用户想要下载的页面的字符串列表
    while True:
        start_page_num = input("输入开始下载的目录页的页码(默认为1,最大为%s): "%myarticle.total_page_num) or "1"
        end_page_num = input("输入结束下载的目录页的页码(默认为1,最大为%s): "%myarticle.total_page_num) or "1"
        if start_page_num.isdigit() and end_page_num.isdigit():
            if int(end_page_num)>=int(start_page_num) and int(end_page_num)<=myarticle.total_page_num and int(start_page_num)<=myarticle.total_page_num:
                break
        else:
            print("无效的页码输入,请重新输入: ")

    start_page_num = int(start_page_num)
    end_page_num = int(end_page_num)

    page_range_str_li = [str(i) for i in range(start_page_num,end_page_num+1)]
    downloaded_file_num = 0
    for page in page_range_str_li:
        myarticle.darticles_one_index(page)
        downloaded_file_num += len(os.listdir(myarticle.sub_file_download_dir))

    print("Finished downloading,%s files have been downloaded!" % downloaded_file_num)


if __name__ == '__main__':

    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    myarticle = DownLoadArticle("http://jhsjk.people.cn/result/")

    start_download(myarticle)