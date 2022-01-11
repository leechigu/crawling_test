# -*- coding: utf-8 -*-

import pandas as pd
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from openpyxl import Workbook

driver = webdriver.Chrome(executable_path='chromedriver')
driver.maximize_window()

write_wb = Workbook();
write_ws = write_wb.active

count = 0

url = 'https://data.seoul.go.kr/dataList/datasetList.do'
driver.get(url)
for j in range (10) :
    for i in range(10):
        count += 1
        # //*[@id="datasetVO"]/div[2]/div/section/div[2]/dl[2]/dt/a/strong
        # //*[@id="datasetVO"]/div[2]/div/section/div[2]/dl[3]/dt/a/strong
        xpathhead = '//*[@id="datasetVO"]/div[2]/div/section/div[2]/dl['
        xpathmiddle = str(i + 1)
        xpathtail = ']/dt/a/strong'
        xpath = xpathhead + xpathmiddle + xpathtail
        driver.find_element(By.XPATH, xpath).click()
        cururl = driver.current_url
        write_ws.cell(count,1, cururl)
        print(count)
        driver.back()
        if count == 7066:
            break;
    if count == 7066:
        break;

    # //*[@id="datasetVO"]/div[2]/div/section/div[2]/div/div/button[4]
    # //*[@id="datasetVO"]/div[2]/div/section/div[2]/div/div/button[13]
    xhead = '//*[@id="datasetVO"]/div[2]/div/section/div[2]/div/div/button['
    xmiddle = str(j+4)
    xtail = ']'
    next_page_xpath = xhead + xmiddle + xtail
    driver.find_element(By.XPATH, next_page_xpath).click()


write_wb.save('seoul_data.xlsx')


# 다음 페이지 버튼 클릭