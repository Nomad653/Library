import sqlite3
from bs4 import BeautifulSoup
import requests
import re
import numpy as np

def bazaya_qosulma():
    try:
        with sqlite3.connect('baza.db') as db:
            cursor = db.cursor()
            print('Baza ilə əlaqə uğurla yaradıldı')
            return db, cursor
    except sqlite3.Error as error:
        print('Xəta baş verdi', error)
        return None, None

def bazaya_yaz(db, cursor, records):
    try:
        data_param = """INSERT INTO kitabxana (kitab_adi, muellif, burax_ili, ISBN, price) VALUES (?, ?, ?, ?, ?)"""
        cursor.executemany(data_param, records)
        db.commit()
        print('Melumat bazaya ugurla elave edildi')
    except sqlite3.Error as error:
        print('Xeta bas verdi', error)



def bazaya_yaz2(db,cursor, kitab_adi=None, muellif=None, burax_ili=None, ISBN=None, price=None):
    try:
        kitab_adi = input('Kitabın adını daxil edin: ')
        muellif = input('Müəllifin adını daxil edin: ')
        burax_ili = int(input('Buraxılış ili daxil edin: '))
        ISBN = input('ISBN daxil edin: ')
        price = input('Veziyyeti: ')

        cursor.execute(
            "INSERT INTO kitabxana (kitab_adi, muellif, burax_ili,ISBN,price) VALUES (?, ?, ?, ?)",
            (kitab_adi, muellif, burax_ili, ISBN, price))
        db.commit()
        print('Melumat bazaya ugurla elave edildi')
    except sqlite3.Error as error:
        print('Xeta bas verdi', error)

def bazaya_yaz3(db,cursor, kitab_adi=None, muellif=None, burax_ili=None, ISBN=None, price=None):
    try:
        kitab_adi = kitab_adi
        muellif = muellif
        burax_ili = burax_ili
        ISBN = ISBN
        price = price

        cursor.execute(
            "INSERT INTO kitabxana (kitab_adi, muellif, burax_ili,ISBN,price) VALUES (?, ?, ?, ?, ?)",
            (kitab_adi, muellif, burax_ili, ISBN, price))
        db.commit()
        print('Melumat bazaya ugurla elave edildi')
    except sqlite3.Error as error:
        print('Xeta bas verdi', error)
        print('kitab_adi:', kitab_adi)
        print('muellif:', muellif)
        print('burax_ili:', burax_ili)
        print('ISBN:', ISBN)
        print('price:', price)

def bazani_yenile(db,cursor,new_list):
    try:
        query_param="""UPDATE kitabxana SET kitab_adi=?, muellif=?, burax_ili=?, ISBN=?, price=? where book_id=?"""
        cursor.executemany(query_param,new_list)
        db.commit()
        print('Bazada', cursor.rowcount,' melumat ugurla yenilendi')
    except sqlite3.Error as error:
        print('Xeta bas verdi', error)



def bazadan_silme(db,cursor,id):
    try:
        del_query="""DELETE FROM kitabxana where book_id =?"""
        cursor.execute(del_query,(id,))
        db.commit()
        print("Melumat bazadan silindi")
    except sqlite3.Error as error:
        print('Xeta bas verdi', error)

def bazani_bagla(db):
    try:
        db.close()
        print("Bazaya ilə əlaqə kəsildi")
    except sqlite3.Error as error:
        print('Xəta baş verdi', error)


#*********************************************************************************************
#
# database_connect, cursor = bazaya_qosulma()
#
#  # bazaya yazmagin 1-ci usulu
# # records = [
# #     ('English', 'Henry', '2022', '4564121324', '15,55'),
# #     ('Tebiet', 'Samir Aslan', '2023', '47894651', '26,78')
# # ]
# #
# # bazaya_yaz(database_connect, cursor, records)
#
#
#  # bazaya yazmagin 2-ci usulu
# bazaya_yaz3(database_connect,cursor,kitab_adi='Sssasas',muellif='dsfdsfd',burax_ili=2122,ISBN="15464646",price="4454")
#
# #
# # # melumatlarin bazada yenilenmesi
# # verilenler=[('English', 'Henry', '2022', '4564121324', '56,45',6),
# #          ('Tebiet', 'Samir Aslan', '2023', '47894651', '99,87',7)]
# #
# # bazani_yenile(database_connect,cursor,verilenler)
# #
# # bazadan_silme(database_connect,cursor,2)
#
# if database_connect:
#     bazani_bagla(database_connect)
# *********************************************************************************
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

