import sqlite3

with sqlite3.connect('baza.db') as db:
    cursor=db.cursor()

    book_query="""CREATE TABLE IF NOT EXISTS kitabxana(
    book_id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
    kitab_adi TEXT,
    muellif TEXT,
    janr TEXT,
    burax_ili INTEGER,
    ISBN TEXT,
    mesgul TEXT    
    )"""

    isciler_query="""CREATE TABLE IF NOT EXISTS isciler(
    id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
    ad TEXT,
    soyad TEXT,
    ata_adi TEXT,
    yash INTEGER,
    books_id INTEGER   
    )"""

    cursor.execute(book_query)
    cursor.execute(isciler_query)
    db.commit()
    print("Database ugurlar yaradildi")






