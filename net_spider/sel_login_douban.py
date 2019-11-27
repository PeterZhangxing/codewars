from selenium import webdriver
import time
import requests
from lxml import etree
# from yundama.dama import identify

driver = webdriver.Chrome()
driver.get("https://www.douban.com/")

# 获取登录前的cookie
s_cookie = {i['name']:i["value"] for i in driver.get_cookies()}
print(s_cookie)

# 切换到iframe
log_iframe = driver.find_element_by_xpath("//div[@class='login']/iframe")
driver.switch_to.frame(log_iframe)

driver.find_element_by_class_name("account-tab-account").click()

# 填写用户名密码
driver.find_element_by_id("username").send_keys("18687027119")
driver.find_element_by_id("password").send_keys("zx20_05")

# # 识别验证码
# #1.找到请求验证码的地址
# captcha_image_url = driver.find_element_by_id("").get_attribute("src")
# #2.再次获取验证码图片
# captcha_pic_content = requests.get(captcha_image_url).content
# #3.将图片放到打码平台，识别图片内容
# captcha_code = identify(captcha_pic_content)
#
# #输入验证码
# driver.find_element_by_id("").send_keys(captcha_code)

# 发送登录请求
time.sleep(3)
# print(driver.find_element_by_xpath("//div[@class='account-form-field-submit']/a[@class='btn btn-account']").text)
driver.find_element_by_link_text("登录豆瓣").click()

# 等待3秒后,获取cookie,关闭浏览器
time.sleep(6)

s_cookie = {i['name']:i["value"] for i in driver.get_cookies()}
# print(s_cookie)

# driver.quit()

# 使用刚才利用selenium获取的cookie,爬取登录后的页面内容
time.sleep(3)
dou_html_str = requests.get(
    url="https://www.douban.com/",
    cookies=s_cookie,
).content.decode()

formated_html = etree.HTML(dou_html_str)
username = formated_html.xpath("//div[@class='top-nav-info']//li[@class='nav-user-account']/a[@class='bn-more']/span[1]/text()")[0]
print(username)