import csv
import random
import time
import string

import requests
from pip._vendor.retrying import retry

with open('../file/IP.csv', 'r') as csvfile:
    # 有表头，字典显示
    reader = csv.DictReader(csvfile)
    rows = [row for row in reader]

with open('../file/isbn.csv', 'r') as csvfile:
    # 有表头，字典显示
    reader = csv.DictReader(csvfile)
    isbn = [row for row in reader]
# url = "https://img3.doubanio.com/lpic/s3237605.jpg"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 '
                  'Safari/537.36 '}


@retry(stop_max_attempt_number=3)
def Crawl(IP):
    response = requests.get(i['url'], headers=headers, proxies={'http': IP}, timeout=4)
    return response


for i in isbn:
    thisip = random.choice(rows)
    if thisip["HTTP"] == "HTTP":
        response = Crawl(thisip["IP"])
        if response.status_code == 200:
            value = ''.join(random.sample(string.ascii_letters + string.digits, 5))
            with open("../src/" + i['isbn'] + "_" + value + '.jpg', 'wb') as f:
                f.write(response.content)
            print("%s  成功" % i["isbn"])
        else:
            print("%s 请求错误" % i['isbn'])
        time.sleep(1)
