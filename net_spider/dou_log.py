from selenium import webdriver
import time
import requests
from lxml import etree
import random


class DouBanSpider(object):

    def __init__(self,username,passwd,browser="Chrome",base_url="https://www.douban.com/"):
        self.base_url = base_url
        if hasattr(webdriver,browser):
            self.driver = getattr(webdriver,browser)()
        else:
            raise NameError("no such browser!")
        if not username or not passwd:
            raise ValueError("username and password cannot be null")
        self.username = username
        self.passwd = passwd
        self.get_logged_cookie()


    def get_logged_cookie(self):
        # 请求豆瓣登录页面
        self.driver.get("https://www.douban.com/")

        # 切换到包括登录信息的iframe
        log_iframe = self.driver.find_element_by_xpath("//div[@class='login']/iframe")
        self.driver.switch_to.frame(log_iframe)

        # 点击，从手机认证码切换至用户名密码登录
        self.driver.find_element_by_class_name("account-tab-account").click()

        # 填写用户名密码
        self.driver.find_element_by_id("username").send_keys(self.username)
        self.driver.find_element_by_id("password").send_keys(self.passwd)

        # 发送登录请求
        sleep_time = random.randint(2,5)
        time.sleep(sleep_time)
        try:
            self.driver.find_element_by_link_text("登录豆瓣").click()
        except Exception as e:
            exit(str(e))

        # 等待3秒后,获取cookie,关闭浏览器
        time.sleep(6)
        self.logged_cookie = {i['name']:i["value"] for i in self.driver.get_cookies()}
        self.driver.quit()


    def get_user_name(self):
        # 使用刚才利用selenium获取的cookie,爬取登录后的页面内容
        dou_html_str = requests.get(
            url="https://www.douban.com/",
            cookies=self.logged_cookie,
        ).content.decode()

        formated_html = etree.HTML(dou_html_str)
        nickname = formated_html.xpath(
            "//div[@class='top-nav-info']//li[@class='nav-user-account']/a[@class='bn-more']/span[1]/text()")[0]
        return nickname.split("的")[0]


if __name__ == '__main__':
    myspider = DouBanSpider("18687027119","zx20_05")
    nick_name = myspider.get_user_name()
    print(nick_name)