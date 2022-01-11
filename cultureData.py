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



def main():
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.maximize_window()

    write_wb = Workbook();
    write_ws = write_wb.active

    url = 'https://kadx.co.kr/product'
    driver.get(url)
    count = 0
    for x in range(3) :
        if x == 0 :
            pagenum = 10
        elif x ==1 :
            pagenum =10
        elif x ==2 :
            pagenum = 5
        for j in range(pagenum):
            for i in range(12):
                count += 1
                time.sleep(1)
                # //*[@id="frmList"]/div/div[3]/div[2]/div/ul/li[1]/a
                # //*[@id="frmList"]/div/div[3]/div[2]/div/ul/li[12]/a
                xpathhead = '//*[@id="frmList"]/div/div[3]/div[2]/div/ul/li['
                xpathmiddle = str(i + 1)
                xpathtail = ']/a'
                xpath = xpathhead + xpathmiddle + xpathtail
                driver.find_element(By.XPATH, xpath).click()
                cururl = driver.current_url
                write_ws.cell(count, 1, cururl)
                print(count)
                driver.back()
                if count == 615:
                    write_wb.save('KADX_Url.xlsx')
                    return

            # //*[@id="frmList"]/div/div[4]/div/span/a[2]
            # //*[@id="frmList"]/div/div[4]/div/span/a[7]
            xhead = '//*[@id="frmList"]/div/div[4]/div/span/a['
            xmiddle = str(j + 3)
            xtail = ']'
            next_page_xpath = xhead + xmiddle + xtail
            driver.find_element(By.XPATH, next_page_xpath).click()




# 다음 페이지 버튼 클릭
