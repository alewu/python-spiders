from bs4 import BeautifulSoup
import requests
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
url = "http://www.qiushibaike.com/"
urls = ['http://www.qiushibaike.com/8hr/page/{}/?s=4943845'.format(str(i)) for i in range(1, 5, 1)]  # 格式化的用法


def get_news(url, data=None):
    time.sleep(4)
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    imgs = soup.select("div.author.clearfix > a:nth-of-type(1) > img")
    names = soup.select("div.author.clearfix > a:nth-of-type(2)")
    ages = soup.select("div.author.clearfix > div")

    for img, name, age in zip(imgs, names, ages):
        data = {
            'img': img.get('src'),
            'name': name.find("h2").get_text(),
            'age': list(age.stripped_strings)

        }
        print(data)


for single_url in urls:
    get_news(single_url)
