import requests
import urllib
import urllib.request

from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/50.0.2661.102 Safari/537.36'}
url0 = 'http://www.yjz9.com/tu/qcmn/'


def get_img_url(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    img_urls = soup.select('ul > li > a > img ')
    i = 0
    for img_url in img_urls:
        img = img_url.get('src')
        urllib.request.urlretrieve(img, '%s.jpg' % i)
        i += 1


get_img_url(url0)
