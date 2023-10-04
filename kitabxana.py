import sqlite3

username=input('İstifadəçi adı daxil edin: ')
password=input('Şifrəni daxil edin: ')

if username=='admin' and password=='admin123':
    print('Səhifəyə uğurla daxil oldunuz')

    try:
        with sqlite3.connect('baza.db') as db:
            cursor = db.cursor()
            print("Baza ile elaqe ugurla yaradildi")

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

            for value in cursor.execute("SELECT * FROM kitabxana"):
                print(value)
    except sqlite3.Error as error:
        print("Xeta bas verdi",error)
    finally:
        db.close()
        print("Database ile elaqe kesildi")

else:
    print("İstifadəçi adı və şifrəsi yanlışdır!!!")


class kitab():
 def __init__(self,id,ad,janr,muellif,buraxilish_ili,ispn_adres):
    self.id = id
    self.ad = ad 
    self.janr = janr
    self.muellif = muellif
    self.buraxilish_ili = buraxilish_ili
    self.ispn_adres = ispn_adres 
 

