# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:26:24 2019

@author: 佑崧
"""

import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 隱藏瀏覽器
chrome_options = Options()
chrome_options.add_argument("--headless")  # 定義 headless
driver = webdriver.Chrome(chrome_options=chrome_options)
url = 'https://pixabay.com/zh/editors_choice/'
driver.get(url)
driver.implicitly_wait(1)


for i in range(1,51):
    # 向下捲動，會花費一些時間
    results = driver.find_elements_by_css_selector("img")
    driver.execute_script("arguments[0].scrollIntoView();", results[i])
    time.sleep(1)

sp = BeautifulSoup(driver.page_source, 'html.parser')

images_dir="images/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

all_links=sp.find_all('img') 
n = 1
for link in all_links:
    src=link.get('src')
    if src != None and ('.jpg' in src or '.png' in src or '.gif' in src):
        filename = src.split('/')[-1]
        print(str(n) + '. ' +src)
        try:
            image = urlopen(src)
            f = open(os.path.join(images_dir,filename),'wb')
            f.write(image.read())
            f.close()
        except:
            print("{} 無法讀取!".format(filename))
        n += 1