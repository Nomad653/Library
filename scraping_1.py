import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# x = Service('.\chromedriver.exe')
# driver = webdriver.Chrome(service=x)
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.kitapyurdu.com/')

driver.find_element(By.XPATH, "//span[@class='mn-strong common-sprite' and text()='Çok Satan Kitaplar']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//a[@class='mn-icon icon-angleRight']//strong[text()='Edebiyat']").click()
time.sleep(3)
driver.find_element(By.ID, 'cookiescript_buttons').click()

kitablar = []

for sehifelerin_sayi in range(1, 16):
    
    kitablarin_adi = driver.find_elements(By.XPATH, "//div[@class='name ellipsis']/a")
    kitablarin_muellifi = driver.find_elements(By.XPATH, "//div[@class='author compact ellipsis']/a[@class='alt']")
    kitablarin_infosu = driver.find_elements(By.XPATH, "//div[@class='product-info']")
    
    #kitablarin isbn i
    isbn_listi = []
    for i in kitablarin_infosu:
        z = i.get_attribute("innerHTML").split('|')
        for isbn in z:
            isbn = isbn.replace(' ', '')
            if str(isbn).isdigit and len(isbn) == 13:
                isbn_listi.append(isbn)

    for i in range(min(len(kitablarin_adi), len(kitablarin_muellifi), len(kitablarin_infosu))):
        kitab = {
           
            "Ad": kitablarin_adi[i].get_attribute('title'),
            "muellif": kitablarin_muellifi[i].text,
            #kitablarin ili
            "kitabin_nesr_ili": kitablarin_infosu[i].get_attribute("innerHTML").split('|')[-1].split('<br>')[-1].strip(),
            "kitabin_isbni": isbn_listi[i] if i < len(isbn_listi) else None
        }
        kitablar.append(kitab)

    if sehifelerin_sayi < 15:
        next_button = driver.find_element(By.XPATH, "//a[contains(@class, 'next')]")
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(3)  

with open('kitablar.json', 'w', encoding='utf-8') as f:
    json.dump(kitablar, f, ensure_ascii=False, indent=4)

driver.quit()
