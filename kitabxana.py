<<<<<<< HEAD
class Isci:
    
   
    def __init__(self, ad, soyad, yas,ata_adi):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ata_adi=ata_adi
    
=======
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


>>>>>>> 2dd9f34153dd5dc6eb50c239aea0081169410a5a
