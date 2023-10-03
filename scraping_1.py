import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service('.\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get('https://www.kitapyurdu.com/')
# edebiyyat ,adi, isbn, yayin tarixi,muellif
edebiyyat=driver.find_element(By.XPATH, "//span[@class='mn-strong common-sprite' and text()='Çok Satan Kitaplar' ]")
time.sleep(3)
driver.quit()