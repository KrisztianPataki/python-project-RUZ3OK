import sqlite3



def adatbmentés(nev, oldal, ugy, elet, szer, hit, csap, fel, étel, jelszo):
    conn = sqlite3.connect("teszt.db")
    print("adatb megnyitása sikeres")
    conn.execute("""CREATE TABLE IF NOT EXISTS karakter
    (nev text ,
    oldal int,
    ugy int,
    elet int,
    szer int,
    hit int,
    csap text,
    fel text,
    étel int,
    jelszo text);""")
    print("tábla létrehozás sikeres")

    cursor = conn.cursor()

    bevitel = "INSERT INTO karakter (nev, oldal, ugy, elet, szer, hit, csap, fel, étel, jelszo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
    adatok = nev, oldal, ugy, elet, szer, hit, csap, fel, étel, jelszo

    cursor.execute(bevitel, adatok)
    conn.commit()

    print("adatbvevitel sikeres")
