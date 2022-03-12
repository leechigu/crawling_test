# -*- coding: utf-8 -*-
import time

from openpyxl import Workbook
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException,TimeoutException,UnexpectedAlertPresentException




url = 'https://www.zigbang.com/home/oneroom/map'

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")

driver = webdriver.Chrome(executable_path='chromedriver', options=options)
driver.maximize_window()
driver.get(url)
driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[1]/form/input').click()
driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/form/input').send_keys('서대문구 창천동')
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[1]/div[2]/div/div[1]/div/div/div[1]/div[2]/div/div/div/ul/li[1]').click()


#//*[@id="__next"]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[4]/div/div[1]/div/div[1]
#//*[@id="__next"]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[5]
#//*[@id="__next"]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[6]

#//*[@id="__next"]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[74]