#adi ,isbn,yayin tarixi ,muellifi
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get("https://www.kitapyurdu.com/index.php?route=product/best_sellers&list_id=19")
time.sleep(6)
kitab_melumatlari = []
kitablar = driver.find_elements(By.CLASS_NAME, "product-grid")
for kitab in kitablar:
    kitab_melumatlari.append(kitab.text)
driver.quit()
with open("C:/Users/Hp Pavilion/Links/scraping1.json", "w", encoding="utf-8") as json_file:
    json.dump(kitab_melumatlari, json_file, ensure_ascii=False, indent=4)
    
print("data Json dosyasi kimi yaddasda saxlanildi")
    