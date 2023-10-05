import sqlite3
from bs4 import BeautifulSoup
import requests
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

        table = soup.find('table')
        if table:
            rows = table.find_all('tr')[1:]
            table_data = []
            for row in rows:
                td_tags = row.find_all('td')
                row_data = [td.text.strip() for td in td_tags]
                table_data.append(row_data)

            for row in rows:
                if "ISBN" in row.text:
                    isbn_td = row.find('td').find_next('td')
                    isbn = isbn_td.text.strip()
                elif "Yayın Tarihi" in row.text:
                    date_td = row.find('td').find_next('td')
                    date = date_td.text.strip()

            kitab_adi = soup.find(class_="pr_header").text.strip()
            muellif = soup.find(class_="pr_producers__link").text.strip()
            price = soup.find(class_='price__item').text.strip()

            print(isbn, date, kitab_adi, muellif, price)

            bazaya_yaz3(database_connect,cursor,kitab_adi=kitab_adi,muellif=muellif,burax_ili=date,ISBN=isbn,price=price)

if database_connect:
    bazani_bagla(database_connect)

