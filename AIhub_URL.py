# -*- coding: utf-8 -*-
from telnetlib import EC

import pandas as pd
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from openpyxl import Workbook

driver = webdriver.Chrome(executable_path='chromedriver')
driver.maximize_window()

write_wb = Workbook();
write_ws = write_wb.active

count = 0

url = 'https://aihub.or.kr/aihub-data/vision/about'
driver.get(url)
for k in range(8):
    for j in range(8):
        if j==0 :
            clicknum = 20
        elif j==1 :
            clicknum = 20
        elif j==2 :
            clicknum = 1
        elif j==3 :
            clicknum = 12
        elif j==4 :
            clicknum = 15
        elif j==5 :
            clicknum = 20
        elif j==6 :
            clicknum = 20
        elif j==7 :
            clicknum = 20
        for i in range(clicknum):
            count += 1
            # //*[@id="block-views-block-8dae-bunlyu-block-5"]/div/div/div/div/ul/li[1]
            # //*[@id="block-views-block-8dae-bunlyu-block-5"]/div/div/div/div/ul/li[48]
            xpathhead = '//*[@id="block-views-block-8dae-bunlyu-block-3"]/div/div/div/div/ul/li['
            xpathmiddle = str(i + 1)
            xpathtail = ']'
            xpath = xpathhead + xpathmiddle + xpathtail
            driver.find_element(By.XPATH,xpath).click()
            cururl = driver.current_url
            write_ws.cell(count, 1, cururl)
            print(count)
            driver.back()
        if  j== 0 :
            driver.find_element(By.XPATH,'//*[@id="block-stig-sub-system-main"]/div/section[2]/div/div[1]/nav/ul/li[2]/a').click()
        elif j==1 :
            driver.find_element(By.XPATH, '//*[@id="block-stig-sub-system-main"]/div/section[2]/div/div[1]/nav/ul/li[3]/a').click()
        elif j==2 :
            driver.find_element(By.XPATH, '//*[@id="block-stig-sub-system-main"]/div/section[2]/div/div[1]/nav/ul/li[4]/a').click()
        elif j==3 :
            driver.find_element(By.XPATH, '//*[@id="block-stig-sub-system-main"]/div/section[2]/div/div[1]/nav/ul/li[5]/a').click()
        elif j==4 :
            driver.find_element(By.XPATH, '//*[@id="block-stig-sub-system-main"]/div/section[2]/div/div[1]/nav/ul/li[6]/a').click()
        elif j==5 :
            driver.find_element(By.XPATH, '//*[@id="block-stig-sub-system-main"]/div/section[2]/div/div[1]/nav/ul/li[7]/a').click()
        elif j==6 :
            driver.find_element(By.XPATH, '//*[@id="block-stig-sub-system-main"]/div/section[2]/div/div[1]/nav/ul/li[8]/a').click()

write_wb.save('AI_Url.xlsx')

# 다음 페이지 버튼 클릭
