# 导入所需要的库
import os
import random
import re
import time
from urllib.request import urlretrieve

from bs4 import BeautifulSoup
import requests

# 创建目录和转换到当前目录
os.mkdir("C:\\Users\hs\Desktop\mm")
os.chdir("C:\\Users\hs\Desktop\mm")
# 多个网页存入列表
urls = ['http://jandan.net/ooxx/page-{}#comments'.format(str(i)) for i in range(2338, 2349, 1)]
# 使用随机表头
my_userAgent = [
    "Mozilla/5.0 (Windows NT 5.1; rv:37.0) Gecko/20100101 Firefox/37.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50",
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/46.0.2490.76 Mobile Safari/537.36"
]
random_userAgent = random.choice(my_userAgent)
url_list = []


def get_url(url):  # 获取每页的图片链接
    headers = {'User-Agent': random_userAgent}
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    imgs = soup.findAll('img', {'src': re.compile("\/\/ww.*\.sinaimg\.cn\/mw600\/[A-Za-z0-9+]+\.jpg")})
    for img in imgs:
        img_url = "http:" + img['src']
        url_list.append(img_url)


for single_url in urls:  # 遍历多页，获得链接
    get_url(single_url)

num = 0
for each_url in url_list:  # 下载图片
    time.sleep(1)
    urlretrieve(each_url, '%s.jpg' % num)
    num += 1
    print(num, each_url)
