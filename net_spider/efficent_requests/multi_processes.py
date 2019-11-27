from concurrent.futures import ProcessPoolExecutor
import requests


# def task(url):
#     response = requests.get(url)
#     print(url,response.content)
#
# pool = ProcessPoolExecutor(3)
#
# url_list = [
#     'http://www.cnblogs.com/wupeiqi',
#     'http://huaban.com/favorite/beauty/',
#     'http://www.baidu.com',
#     'http://www.autohome.com.cn',
# ]
#
# for url in url_list:
#     pool.submit(task,url)
#
# pool.shutdown(wait=True)


def task(url):
    response = requests.get(url)
    return response

def done(future,*args,**kwargs):
    response = future.result() # equal task's response
    print(response.status_code,response.content)

pool = ProcessPoolExecutor(3)

url_list = [
    'http://www.cnblogs.com/wupeiqi',
    'http://huaban.com/favorite/beauty/',
    'http://www.baidu.com',
    'http://www.autohome.com.cn',
]

for url in url_list:
    v = pool.submit(task,url)
    v.add_done_callback(done)

pool.shutdown(wait=True)