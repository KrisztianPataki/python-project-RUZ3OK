import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import jatek
class user:
    nev = ""
    jelszo = ""
    old = 0


def regisztral(regnev,regjel):
    user.jelszo = regjel
    user.nev = regnev
    user.old = 0
    print(user.jelszo, user.nev)
    file = open("mentes.txt", "a")
    file.write(str(user.nev)+","+str(user.jelszo)+","+str(user.old)+"\n")
    file.close()
    jatek.lapok(user.nev, user.old)


def bejel(bejnev,bejjel):
    try:
        nev = bejnev
        jelszo = bejjel
        adatjo = 0
        bejfile = open("mentes.txt", "r")

        for i in bejfile:

            szovtom = i.split(",")
            print(szovtom[0])
            print(szovtom[1])
            if szovtom[0] == nev and szovtom[1] == jelszo:
                adatjo = 1
                user.nev = szovtom[0]
                user.old = szovtom[2]
        if adatjo == 1:
            print("létezik ilyen felhasználó")
            print(user.old)
            jatek.lapok(user.nev, user.old)
        else:
            print("nem találtam ilyen felhasználót")

    except:
        messagebox.showerror("nem tudtam megnyitni a mentés filet/nincs felhasználó regisztrálva ezen a gépen")


