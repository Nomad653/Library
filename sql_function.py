import sqlite3

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