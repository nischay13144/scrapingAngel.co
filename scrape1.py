import os
import sys

import wget

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://angel.co/companies")

WebDriverWait(driver, 100).until( lambda driver: driver.find_elements_by_xpath('//*[@id="root"]/div[4]/div[2]/div/div[2]/div[2]/div[2]'))
driver.find_element_by_class_name('more').click()


for num in range(2,22):
    titles_element = driver.find_elements_by_xpath('//*[@id="root"]/div[4]/div[2]/div/div[2]/div[2]/div[2]/div[' + str(num) + ']')
    titles = [x.text for x in titles_element]
    print(titles[0])
    print('\n')
