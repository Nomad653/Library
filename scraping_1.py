import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
x = Service('.\chromedriver.exe')
driver = webdriver.Chrome(service=x)
driver.maximize_window()
driver.get('https://www.kitapyurdu.com/')

# edebiyyat ,adi, isbn, yayin tarixi,muellif

edebiyyat=driver.find_element(By.XPATH, "//span[@class='mn-strong common-sprite' and text()='Çok Satan Kitaplar']").click()
time.sleep(1)
cok_satilan=driver.find_element(By.XPATH,"//a[@class='mn-icon icon-angleRight']//strong[text()='Edebiyat']").click()
accept=driver.find_element(By.ID,'js-popup-accept-button').click()

time.sleep(3)

driver.quit()
