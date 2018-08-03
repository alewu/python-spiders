import urllib.request
from bs4 import BeautifulSoup
import requests
import re
import os
import time

url = "http://www.easyicon.net/iconsearch/iconset:Control-icons/"
headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 5.1; rv:37.0) Gecko/20100101 Firefox/37.0"}
wb_data = requests.get(url, headers = headers)
soup = BeautifulSoup(wb_data.text,'lxml')
pattern = "^http.*\/png\/"
# http://download.easyicon.net/png/1205812/524/
images = soup.findAll("a", {"href": re.compile(pattern)})
os.mkdir("C:\\Users\hs\Desktop\mm")
os.chdir("C:\\Users\hs\Desktop\mm")
count = 0
for img in images:
    time.sleep(1)
    #urllib.request.urlretrieve(img, 'gh')
    count += 1
    print(count, img["href"])