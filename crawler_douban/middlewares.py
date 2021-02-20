# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import csv

from scrapy import signals
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import random
from crawler_douban.settings import IPPOOL
# from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
# from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

from crawler_douban.settings import USER_AGENT_LIST

with open('file/check_ip.csv', 'r') as csvfile:
    # 有表头，字典显示
    reader = csv.DictReader(csvfile)
    rows = [row for row in reader]


# user-agent池
class RotateUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua = random.choice(USER_AGENT_LIST)
        if ua:
            request.headers['User-Agent'] = ua  # 请求头是一个字典
            # print(ua)


# IP代理池
class IPPOOLS(object):

    def process_request(self, request, spider):
        """现没用随机ip，如使用文件内ip，添加读取文件进行循环或随机，只支持http"""
        thisip = random.choice(rows)
        print("当前使用的IP为： " + thisip["IP"])
        request.meta["proxy"] = "http://" + thisip["IP"]

