import csv

import scrapy
import random
import string
import os


class DoubanSrcSpider(scrapy.Spider):
    name = 'douban_src'
    allowed_domains = ['douban.com']
    # start_urls = ['https://book.douban.com/isbn/9787220120725/']

    def start_requests(self):
        # 读取文件的isbn和url
        with open('crawler_douban/file/isbn.csv', 'r') as csvfile:
            # 有表头，字典显示
            reader = csv.DictReader(csvfile)
            rows = [row for row in reader]
        for i in rows:
            yield scrapy.Request(i["url"], self.parse, meta={"item": i["isbn"]}, dont_filter=True)

    def parse(self, response):
        itme = response.meta['item']
        if response.status == 200:
            print("请求成功:" + str(response.status), response.url)
        else:
            print("请求失败:" + str(response.status), response.url)
            with open('../file/error.csv', 'a', encoding="utf-8") as f:
                f.write("%s,%s\n" % (itme, str(response.status)))
            return
        link = response.xpath('//*[@id="mainpic"]/a/@href').extract_first()
        if link:
            yield scrapy.Request(url=link, callback=self.src_parse, meta={"item": itme}, dont_filter=True)

    def src_parse(self, response):
        itme = response.meta['item']
        value = ''.join(random.sample(string.ascii_letters + string.digits, 5))
        with open("crawler_douban/src/"+itme+"_"+value+".jpg", "wb") as f:
            f.write(response.body)
