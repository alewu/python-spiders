from bs4 import BeautifulSoup
import requests
import time

url = 'http://www.yjz9.com/tu/qcmn/'
urls = ['http://www.yjz9.com/tu/qcmn/{}.shtml'.format(str(i)) for i in range(2, 5, 1)]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def get_page(url, data=None):
    time.sleep(2)
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('ul > li > a > div')
    imgs_links = soup.select('ul > li > a > img')

    for title, img_link in zip(titles, imgs_links):
        data = {
            'img_link': img_link.get('src'),
            'title': title.get_text()
        }
        print(data)


for single_page in urls:
    get_page(single_page)
