import requests
import time
from functools import wraps

'''
常用的代理服务器查询网站：
https://proxy.mimvp.com/freeopen.php
'''

def outter(f):
    @wraps(f)
    def inner(*args,**kwargs):
        start_time = time.time()
        res = f(*args,**kwargs)
        stop_time = time.time()
        print(stop_time - start_time)
        return res
    return inner


proxies = {
    "http":"http://60.205.188.24:3128"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3521.2 Safari/537.36"
}

url = "http://www.baidu.com"

@outter
def test_reqproxy():
    res = requests.get(
        url=url,
        headers=headers,
        # 不是自己直接访问网站，而是通过以下的正向代理去访问指定的url
        proxies=proxies,
    )
    return res

if __name__ == '__main__':
    print(test_reqproxy().content.decode())