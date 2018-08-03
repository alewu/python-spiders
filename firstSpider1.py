import time
from bs4 import BeautifulSoup
import requests
import csv

urls = ['http://mobile.yundingqianzhuang.net/index.php?s=/Agent/Index/user_list/token/NjBmYVlzZmR1QUJKTmd3ZUZLek91dUQ4NjFFTjcwWlhUNHdHdTJ5UW5jOXBOZjRCS0hJ/p/{}.html'.format(
        str(i)) for i in range(1, 584, 1)]  # 格式化的用法

data_list = []  # 结构: [dict1, dict2, ...], dict结构{'船名': ship_name, '航次': voyage, '提单号': bill_num, '作业码头': wharf}


def get_attractions(url, data=None):
    headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36"}

    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    for idx, ul in enumerate(soup.find_all('ul')):
        if idx != 0:
            lis = ul.find_all('li')
            data_list.append({
                'ID': lis[0].contents[0],
                'name': lis[1].contents[0],
                'phone': lis[2].contents[0],
                'faction': lis[3].contents[0].strip(),
                'time': lis[4].contents[0]
            })


for u in urls:
    print(u)
    time.sleep(1)
    get_attractions(u)
print(data_list)
print(len(data_list))

with open('data.csv', 'w', newline='', encoding='utf-8-sig') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['ID', '姓名', '手机号', '设备', '注册时间'])
    for d in data_list:
        writer.writerow([d["ID"], d["name"], d["phone"], d["faction"], d["time"]])
