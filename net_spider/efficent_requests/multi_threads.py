from concurrent.futures import ThreadPoolExecutor
import requests,time

# def task(url):
#     '''
#     dealing with every request
#     :param url:
#     :return:
#     '''
#     response = requests.get(url=url)
#     print(url,response.text)
#
# # defined how many threads can run at a given time
# pool = ThreadPoolExecutor(3)
#
# url_list = [
#     'http://www.cnblogs.com/wupeiqi',
#     'http://huaban.com/favorite/beauty/',
#     'http://www.zhihu.com',
#     'http://www.sina.com',
#     'http://www.baidu.com',
#     'http://www.autohome.com.cn',
# ]
# start_time =  time.time()
# for url in url_list:
#     pool.submit(task,url)
#
# #this process will wait for all the thread to finish running before it ends.
# pool.shutdown(wait=True)
#
# print("total time spent: ",time.time()-start_time)


def task(url):
    """
    下载页面
    :param url:
    :return:
    """
    response = requests.get(url)
    return response

def done(future,*args,**kwargs):
    '''
    callback function to deal with the returned result from task
    :param future:
    :param args:
    :param kwargs:
    :return:
    '''
    response = future.result()
    print(response.status_code,response.content)

pool = ThreadPoolExecutor(3)
url_list = [
    'http://www.cnblogs.com/wupeiqi',
    'http://huaban.com/favorite/beauty/',
    'http://www.baidu.com',
    'http://www.autohome.com.cn',
]

for url in url_list:
    v = pool.submit(task,url)
    # add a callback function which will be running
    # after getting result from the task function
    # to every separated task function
    v.add_done_callback(done)

pool.shutdown(wait=True)