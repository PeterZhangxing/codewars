from twisted.internet import defer
# from twisted.web.client import getPage
from twisted.internet import reactor
from twisted.web.client import Agent

def one_done(arg):
    print(arg)

def all_done(arg):
    print('done')
    reactor.stop()

@defer.inlineCallbacks
def task(url):
    # res = getPage(bytes(url, encoding='utf8')) # 发送Http请求
    res = Agent(bytes(url, encoding='utf8')) # 发送Http请求
    res.addCallback(one_done)
    yield res

url_list = [
    'https://www.baidu.com/',
    'https://www.taobao.com/',
    'https://www.jd.com/',
    'https://www.bilibili.com/',
]

defer_list = [] # [特殊，特殊，特殊(已经向url发送请求)]
for url in url_list:
    v = task(url)
    defer_list.append(v)

d = defer.DeferredList(defer_list)
d.addBoth(all_done)


reactor.run() # 死循环