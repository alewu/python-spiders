import os
import re
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

homepage_link = 'http://www.ivrfans.cn'
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/46.0.2490.76 Mobile Safari/537.36'}


def get_web_code(url):
    web_code = requests.get(url, headers)
    soup = BeautifulSoup(web_code.text, 'lxml')
    return soup


def get_genre_links(start, end):
    genre_links = ['http://www.ivrfans.cn/xingge/qingchun/list_38_{}.html'.format(str(i)) for i in range(start, end, 1)]
    return genre_links


def get_page_links(page_url):
    imgs1 = get_web_code(page_url).findAll('a', {"href": re.compile("\/xingge\/qingchun\/[0-9]+\.html")})
    url_list1 = []
    for img1 in imgs1:
        whole_url = homepage_link + img1['href']
        url_list1.append(whole_url)
    return url_list1


def get_img_links(img_url):
    imgs2 = get_web_code(img_url).findAll('img', {
        "src": re.compile("http:\/\/mimg\.xmeise\.com\/thumb\/m\/allimg\/[0-9]+\/1\-[A-Z0-9]+\.jpg")})
    url_list2 = []
    for img2 in imgs2:
        img_url2 = img2['src']
        url_list2.append(img_url2)
    return url_list2


def download_pic(url):
    os.mkdir("C:\\Users\hs\Desktop\mm")
    os.chdir("C:\\Users\hs\Desktop\mm")
    for each in img_list:
        file_name = each.split('/')[-1]
        with open(file_name, 'wb') as pic:
            img = urlopen(url)
            pic.write(img)


img_list = []
for genre_link in get_genre_links(1, 2):
    for link in get_page_links(genre_link):
        img_list.append(get_img_links(link)[0])

for img in img_list:
    download_pic(img)
