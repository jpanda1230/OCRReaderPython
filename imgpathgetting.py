

from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import json


try:
    driver = webdriver.Chrome("chromedriver.exe")
    driver.set_page_load_timeout(20)

    driver.get("https://localhost/ooo")
    #driver.get("https://localhost/zzz")
    time.sleep(10)

    #driver.get("https://www.norsk-tipping.no/sport/langoddsen")
    html = driver.page_source
    soup=BeautifulSoup(html,'lxml')
    title_list = soup.find_all('a', 'competitionId1185')
    for title in title_list:
        print(title.text)

    images = driver.find_elements_by_tag_name('img')
    pngPath =[]
    for image in images:
        pngPath.append(image.get_attribute('src'))
        print(image.get_attribute('src'))

    print(pngPath[4])
finally:
    print("123")


