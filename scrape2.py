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


for num in range(2,20):
    driver.find_element_by_xpath('//*[@id="root"]/div[4]/div[2]/div/div[2]/div[2]/div[2]/div['+ str(num) +']/div/div[1]/div/div[2]/div[1]/a').click()

    titles_element = driver.find_elements_by_xpath("//*[@class='larger roles']")
    titles = [x.text for x in titles_element]
    if titles[0]:
        print(titles[0])
        print('\n')
    driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[1]/div[2]/div/li[4]/a').click()
    driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[1]/div[2]/div/li[4]/div/div/div[3]/a[1]').click()
    WebDriverWait(driver, 100).until( lambda driver: driver.find_elements_by_xpath('//*[@id="root"]/div[4]/div[2]/div/div[2]/div[2]/div[2]'))
