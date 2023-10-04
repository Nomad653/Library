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
        data_param = """INSERT INTO kitabxana (kitab_adi, muellif, janr, burax_ili, ISBN, mesgul) VALUES (?, ?, ?, ?, ?, ?)"""
        cursor.executemany(data_param, records)
        db.commit()
        print('Melumat bazaya ugurla elave edildi')
    except sqlite3.Error as error:
        print('Xeta bas verdi', error)



def bazaya_yaz2(db,cursor, kitab_adi=None, muellif=None, janr=None, burax_ili=None, ISBN=None, mesgul=None):
    try:
        kitab_adi = input('Kitabın adını daxil edin: ')
        muellif = input('Müəllifin adını daxil edin: ')
        janr = input('Janrın adını daxil edin: ')
        burax_ili = int(input('Buraxılış ili daxil edin: '))
        ISBN = input('ISBN daxil edin: ')
        mesgul = input('Veziyyeti: ')

        cursor.execute(
            "INSERT INTO kitabxana (kitab_adi, muellif, janr, burax_ili,ISBN,mesgul) VALUES (?, ?, ?, ?, ?, ?)",
            (kitab_adi, muellif, janr, burax_ili, ISBN, mesgul))
        db.commit()
        print('Melumat bazaya ugurla elave edildi')
    except sqlite3.Error as error:
        print('Xeta bas verdi', error)

def bazani_yenile(db,cursor,new_list):
    try:
        query_param="""UPDATE kitabxana SET kitab_adi=?, muellif=?, janr=?, burax_ili=?, ISBN=?, mesgul=? where book_id=?"""
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

database_connect, cursor = bazaya_qosulma()

 # bazaya yazmagin 1-ci usulu
records = [
    ('English', 'Henry', 'derslik', '2022', '4564121324', 'elde'),
    ('Tebiet', 'Samir Aslan', 'derslik', '2023', '47894651', 'elde')
]

bazaya_yaz(database_connect, cursor, records)


 # bazaya yazmagin 2-ci usulu
bazaya_yaz2(database_connect,cursor)


# melumatlarin bazada yenilenmesi
verilenler=[('English', 'Henry', 'derslik', '2022', '4564121324', 'elde',6),
         ('Tebiet', 'Samir Aslan', 'derslik', '2023', '47894651', 'elde',7)]

bazani_yenile(database_connect,cursor,verilenler)

bazadan_silme(database_connect,cursor,2)

if database_connect:
    bazani_bagla(database_connect)

