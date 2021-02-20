import csv

import scrapy



class DoubanSrcSpider(scrapy.Spider):
    name = 'kdl'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/inha/2/']

    def parse(self, response):
        if response.status == 200:
            print("请求成功:" + str(response.status), response.url)
        else:
            print("请求失败:" + str(response.status), response.url)
        data = response.xpath('//*[@id="content"]')
        list = data.xpath('//*[@id="list"]/table/tbody/tr')
        for i in range(len(list)):

            ip = data.xpath('//*[@id="list"]/table/tbody/tr['+str(i+1)+']/td[1]/text()').extract_first()
            port = data.xpath('//*[@id="list"]/table/tbody/tr['+str(i+1)+']/td[2]/text()').extract_first()
            type = data.xpath('//*[@id="list"]/table/tbody/tr['+str(i+1)+']/td[4]/text()').extract_first()

            print("%s:%s,%s" % (ip, port, type))
    # def src_parse(self, response):
    #     itme = response.meta['item']
    #     value = ''.join(random.sample(string.ascii_letters + string.digits, 5))
    #     with open("crawler_douban/src/"+itme+"_"+value+".jpg", "wb") as f:
    #         f.write(response.body)
