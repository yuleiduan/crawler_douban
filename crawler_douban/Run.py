# -*- coding: utf-8 -*-
from scrapy.cmdline import execute
import csv
import os
import minium
if __name__ == '__main__':
    execute(['scrapy', 'crawl', 'kdl'])
# 执行文件


# print('***获取当前目录***')
# print(os.getcwd())
# print(os.path.abspath(os.path.dirname(__file__)))
#
# print('***获取上级目录***')
# print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
# print(os.path.abspath(os.path.dirname(os.getcwd())))
# print(os.path.abspath(os.path.join(os.getcwd(), "..")))
#
# print('***获取上上级目录***')
# print(os.path.abspath(os.path.join(os.getcwd(), "../..")))
#
#
# with open('crawler_douban/file/isbn.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     rows = [row for row in reader]
# print(rows)
