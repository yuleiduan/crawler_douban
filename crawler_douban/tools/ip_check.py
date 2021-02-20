import csv

import requests


url = "https://img3.doubanio.com/lpic/s3237605.jpg"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 '
                  'Safari/537.36 '
}
with open('../file/IP.csv', 'r') as csvfile:
    # 有表头，字典显示
    reader = csv.DictReader(csvfile)
    rows = [row for row in reader]
print(rows)
for i in rows:
    if i["HTTP"] == "HTTP":
        try:
            response = requests.get(url, headers=headers, proxies={'http': i["IP"]}, timeout=4)
            if response.status_code == 200:
                print("请求成功%s，%s 代理IP有效！" % (response.status_code, i["IP"]))
                with open('../file/check_ip.csv', 'a', encoding="utf-8") as f:
                    f.write("%s,%s\n" % (i["IP"], i["HTTP"]))
        except Exception as e:
            print(f"请求失败，代理IP无效！{e}")

