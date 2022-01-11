# -*- coding: utf-8 -*-

import pandas as pd
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook



write_wb = Workbook();
write_ws = write_wb.active
count = 0
for t in range(50) :

    urlhead = 'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=&detailKeyword=&publicDataPk=&recmSe=N&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=updtDt&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage='
    urlpagenum = str(t+1)
    urltail ='&perPage=1000&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode='
    url = urlhead + urlpagenum + urltail
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url)
    for i in range(1000):
        count += 1
        string1 = '//*[@id="fileDataList"]/div[2]/ul/li['
        num = str(i + 1)
        string2 = ']/dl/dt/a'
        boardText = driver.find_element(By.XPATH, string1 + num + string2)
        hrefText = boardText.get_attribute('href')
        print(count)
        write_ws.cell(count, 1, hrefText)

write_wb.save('50000.xlsx')




