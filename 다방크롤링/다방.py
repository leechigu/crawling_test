# -*- coding: utf-8 -*-
import time

from openpyxl import Workbook
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException,TimeoutException,UnexpectedAlertPresentException


url = 'https://www.dabangapp.com/search/map?filters=%7B%22multi_room_type%22%3A%5B0%2C1%2C2%5D%2C%22selling_type%22%3A%5B0%2C1%2C2%5D%2C%22deposit_range%22%3A%5B0%2C999999%5D%2C%22price_range%22%3A%5B0%2C999999%5D%2C%22trade_range%22%3A%5B0%2C999999%5D%2C%22maintenance_cost_range%22%3A%5B0%2C999999%5D%2C%22room_size%22%3A%5B0%2C999999%5D%2C%22supply_space_range%22%3A%5B0%2C999999%5D%2C%22room_floor_multi%22%3A%5B1%2C2%2C3%2C4%2C5%2C6%2C7%2C-1%2C0%5D%2C%22division%22%3Afalse%2C%22duplex%22%3Afalse%2C%22room_type%22%3A%5B1%2C2%5D%2C%22use_approval_date_range%22%3A%5B0%2C999999%5D%2C%22parking_average_range%22%3A%5B0%2C999999%5D%2C%22household_num_range%22%3A%5B0%2C999999%5D%2C%22parking%22%3Afalse%2C%22short_lease%22%3Afalse%2C%22full_option%22%3Afalse%2C%22built_in%22%3Afalse%2C%22elevator%22%3Afalse%2C%22balcony%22%3Afalse%2C%22safety%22%3Afalse%2C%22pano%22%3Afalse%2C%22deal_type%22%3A%5B0%2C1%5D%7D&position=%7B%22location%22%3A%5B%5B126.6309765%2C37.2474417%5D%2C%5B127.3979595%2C37.7404793%5D%5D%2C%22center%22%3A%5B127.01446798508894%2C37.494367328004216%5D%2C%22zoom%22%3A11%7D&search=%7B%22id%22%3A%22%22%2C%22type%22%3A%22%22%2C%22name%22%3A%22%22%7D&tab=all'

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")

driver = webdriver.Chrome(executable_path='chromedriver', options=options)
driver.maximize_window()
driver.get(url)
driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[1]/form/input').click()
driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/form/input').send_keys('서대문구 대신동')
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[1]/div[2]/div/div[1]/div/div/div[1]/div[2]/div/div/div/ul/li[1]/div').click()

time.sleep(3)
action = ActionChains(driver)

time.sleep(4)

count =

for i  in range():
    try :
        contents = driver.find_element(By.CSS_SELECTOR,
                                       '#content > div.styled__Content-sc-1nnkzie-0.OjqKy > div.styled__ListWrap-sc-5dgg47-0.kGOyKU '
                                       '> div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > '
                                       'ul.styled__ItemList-sc-5dgg47-2.styled__NormalList-vhzehm-2.bQZezw.cyoDft')
    except NoSuchElementException : #마지막 페이지거나 페이지가 1개일 때 해당 처리
        contents = driver.find_element(By.CSS_SELECTOR,
                                       '#content > div.styled__Content-sc-1nnkzie-0.OjqKy > div.styled__ListWrap-sc-5dgg47-0.kGOyKU > '
                                       'div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > ul')
    list = contents.find_elements(By.TAG_NAME, 'li')
    for li in list:
        title = li.find_element(By.TAG_NAME, 'h1').text
        print(title)
    driver.find_element(By.CSS_SELECTOR,
                        '#content > div.styled__Content-sc-1nnkzie-0.OjqKy > div.styled__ListWrap-sc-5dgg47-0.kGOyKU > div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > ul > li:nth-child(4) > button').click()
