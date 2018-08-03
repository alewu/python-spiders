import requests
from bs4 import BeautifulSoup
import csv

urls = [
    'http://mobile.yundingqianzhuang.net/index.php?s=/Agent/Index/user_list/token/NjBmYVlzZmR1QUJKTmd3ZUZLek91dUQ4NjFFTj' \
    'cwWlhUNHdHdTJ5UW5jOXBOZjRCS0hJ/p/{}.html'.format(str(i)) for i in range(1, 5, 1)]  # 格式化的用法
data_list = []


def get_attractions(url, data=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    wb_data = requests.get(url, headers=headers)

    soup = BeautifulSoup(wb_data.text, 'lxml')
    phones = soup.select('#form > div > ul > li.phone')
    names = soup.select('#form > div > ul > li.name')

    for name, phone in zip(names, phones):
        data = {
            'name': name.get_text(),
            'phone': phone.get_text()
        }
        data_list.append(data)
        print(data)


for url in urls:
    get_attractions(url)

print(len(data_list))

with open('data.csv', 'w', encoding='utf-8-sig') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['name', 'phone'])
    for d in data_list:
        writer.writerow([d["name"], d["phone"]])
