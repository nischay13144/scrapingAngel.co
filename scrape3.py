#Jon Dahl Founder of Mux
#jondahl@mux.com
#jon.dahl@mux.com
#jon@mux.com
#dahl@mux.com
import os
import sys

import wget
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
username = "Jon Dahl"
domain = "mux.com"

driver = webdriver.Chrome()
driver.get("http://emailmatcher.com/")

uname = driver.find_element_by_id("person-name")
uname.send_keys(username)

dname = driver.find_element_by_id("company-domain")
dname.send_keys(domain)
#driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]').is_selected()
recaptcha = driver.find_element_by_xpath("//*[@role='presentation']")
recaptcha.click()
time.sleep(5)
submit_button = driver.find_element_by_id("submit-button").click()
time.sleep(12)  #Giving it 12 seconds to fetch results, may take even more
emailResult = driver.find_element_by_id("email-result")
print emailResult.text
emailWarning = driver.find_element_by_id("warning")
warning = emailWarning.text
if warning:
    print warning
else:
    print "Found"
