
#coinmarketcap
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from openpyxl import Workbook

driver = webdriver.Chrome(executable_path='chromedriver')
driver.maximize_window()

url = "https://coinmarketcap.com/ko/currencies/solana/"
driver.get(url)

price_sol = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span').text
price_sol = price_sol[1:len(price_sol)-3]
temp =''
for i in price_sol:
    if i!=',':
        temp+=i

price_sol = temp
print(price_sol)

url = "https://coinmarketcap.com/ko/currencies/binance-usd/"
driver.get(url)



price_busd = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/span').text
price_busd = price_busd[1:len(price_busd)-3]
temp =''
for i in price_busd:
    if i!=',':
        temp+=i
price_busd = temp
print(price_busd)





