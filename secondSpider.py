from bs4 import BeautifulSoup
import requests
import time

url = 'https://knewone.com/discover?page='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def get_page(url, data=None):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    titles = soup.select('section.content > h4 > a')
    imgs = soup.select('a.cover-inner > img')
    links = soup.select('section.content > h4 > a')

    for title, img, link in zip(titles, imgs, links):
        data = {
            'title': title.get('title'),
            'img': img.get('src'),
            'link': link.get('href')
        }
        print(data)


'''创建获得一个网页的代码的函数'''


def get_more_pages(start, end):
    for i in range(start, end):
        get_page(url + str(i))
        time.sleep(2)


'''创建一个控制获取的页数的函数'''

get_more_pages(1, 5)
