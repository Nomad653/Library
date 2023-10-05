import sqlite3
from bs4 import BeautifulSoup
import requests
import re
import numpy as np
from sql_function import bazaya_qosulma, bazaya_yaz3, bazani_bagla


database_connect, cursor = bazaya_qosulma()

pages=np.arange(1,2)

for page in pages:
    url="https://www.kitapyurdu.com/index.php?route=product/category&page="+str(page)+"&filter_category_all=true&path=1_128&filter_in_stock=1&sort=purchased_365&order=DESC"
    # url="https://www.kitapyurdu.com/index.php?route=product/category/&filter_category_all=true&category_id=128&sort=purchased_365&order=DESC&filter_in_stock=1"
    sehife = requests.get(url)
    soup = BeautifulSoup(sehife.content,"html.parser")


    kitab_link = soup.find_all(class_='name ellipsis')

    list_test=[]
    TableValues=[]
    database=[]

    for x in kitab_link:
        list_test.append(x.a['href'])

    umumi_siyahi = []
    for link in list_test:
        print(link)
        web = requests.get(link)
        soup = BeautifulSoup(web.content, "html.parser")

        TableBody = soup.body

        TableValues = []

        for i in TableBody.find_all('tr'):
            if "ISBN" in i.text:
                isbn_td = i.find('td')
                number_td = isbn_td.find_next('td')
                number1 = number_td.text.strip()
                # print(number1)

        for i in TableBody.find_all('tr'):
            if "Yayın Tarihi" in i.text:
                isbn_td = i.find('td')
                number_td = isbn_td.find_next('td')
                date1 = number_td.text.strip()
                # print(date1)

        kitab_adi = soup.find(class_="pr_header")
        kitab=kitab_adi.text.strip()

        muellif = soup.find(class_="pr_producers__link")
        author=muellif.text.strip()

        price = soup.find(class_='price__item')
        qiymet=price.text.strip()

        umumi_siyahi = [number1, date1, kitab, author, qiymet]
        print(umumi_siyahi)

        bazaya_yaz3(database_connect,cursor,kitab_adi=kitab,muellif=author,burax_ili=date1,ISBN=number1,price=qiymet)

if database_connect:
    bazani_bagla(database_connect)

