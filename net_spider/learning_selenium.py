from selenium import webdriver
import time

# 实例化一个浏览器
driver = webdriver.Chrome()

# 设置浏览器窗口大小
driver.set_window_size(720,580)

# 最大化浏览器窗口
# driver.maximize_window()

# 发送get请求
driver.get("http://www.baidu.com")

# 进行页面截屏
driver.save_screenshot("baidu.png")

# 元素定位的方法
# 在输入框中填上数据
driver.find_element_by_id("kw").send_keys("python")
# 点击按钮
driver.find_element_by_id("su").click()

# driver 获取html字符串
print(driver.page_source) #浏览器中elements的内容

# 获取当前访问的网页的url地址
print(driver.current_url)

# 获取当前页面的cookie
cookies = driver.get_cookies()
print(cookies)

print("*"*100)
# 提取cookie的值为大字典的键值对类型，去掉不必要的字段
cookies = {i["name"]:i["value"] for i in cookies}
print(cookies)
'''
[{'domain': '.baidu.com', 'httpOnly': False, 'name': 'H_PS_PSSID', 'path': '/', 'secure': False, 'value': '1451_21090_18559_29063_28519_29098_28831_26350'}, 
{'domain': '.baidu.com', 'httpOnly': False, 'name': 'delPer', 'path': '/', 'secure': False, 'value': '0'}, 
{'domain': '.baidu.com', 'expiry': 3706529667.533797, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': '8E97E009D766850A4C7CF6118DC69D26:FG=1'},
{'domain': '.baidu.com', 'expiry': 3706529667.533939, 'httpOnly': False, 'name': 'PSTM', 'path': '/', 'secure': False, 'value': '1559046020'},
{'domain': '.baidu.com', 'expiry': 3706529667.533876, 'httpOnly': False, 'name': 'BIDUPSID', 'path': '/', 'secure': False, 'value': '8E97E009D766850A4C7CF6118DC69D26'}, 
{'domain': 'www.baidu.com', 'httpOnly': False, 'name': 'BD_HOME', 'path': '/', 'secure': False, 'value': '0'}, 
{'domain': '.baidu.com', 'expiry': 1559132421.423982, 'httpOnly': False, 'name': 'BDORZ', 'path': '/', 'secure': False, 'value': 'B490B5EBF6F3CD402E515D22BCDA1598'}, 
{'domain': 'www.baidu.com', 'expiry': 1559910021, 'httpOnly': False, 'name': 'BD_UPN', 'path': '/', 'secure': False, 'value': '12314753'}, 
{'domain': 'www.baidu.com', 'expiry': 1559046032, 'httpOnly': False, 'name': 'WWW_ST', 'path': '/', 'secure': False, 'value': '1559046022071'}]
***************************************************************
{'H_PS_PSSID': '1451_21090_18559_29063_28519_29098_28831_26350', 'delPer': '0', 
'BAIDUID': '8E97E009D766850A4C7CF6118DC69D26:FG=1', 'PSTM': '1559046020', 
'BIDUPSID': '8E97E009D766850A4C7CF6118DC69D26', 'BD_HOME': '0', 
'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598', 'BD_UPN': '12314753', 'WWW_ST': '1559046022071'}
'''

# 关闭浏览器
time.sleep(3)
driver.quit()