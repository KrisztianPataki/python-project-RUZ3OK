import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import jatek
import random
class user:
    nev = ""
    jelszo = ""
    old = 0
    ügy = 0
    élet = 0
    szerencse = 0
    hit = 0
    csapások = "semmi"
    felszerelés = "kard,pajzs,hátizsák,lámpás"
    étel = 10

def regisztral(regnev,regjel):
    user.jelszo = regjel
    user.nev = regnev
    user.old = "nulla"
    user.ügy = random.randint(1, 6) + 6
    user.élet = random.randint(2, 12) + 12
    user.szerencse = random.randint(1, 6) + 6
    user.hit = random.randint(1, 6) + 3
    print(user.nev, user.jelszo+"oldal:"+user.old+"szerencse"+str(user.szerencse)+"ügyesség:"+str(user.ügy)+"élet:"+str(user.élet)+"hit:"+str(user.hit)+"csapások:"+str(user.csapások)+"felsz:"+str(user.felszerelés)+"étel:"+str(user.étel))
    file = open("mentes.txt", "a")
    file.write(str(user.nev)+"|"+str(user.jelszo)+"|"+str(user.old)+"|"+str(user.szerencse)+"|"+str(user.ügy)+"|"+str(user.élet)+"|"+str(user.hit)+"|"+str(user.csapások)+"|"+str(user.felszerelés)+"|"+str(user.étel)+"\n")
    file.close()

    jatek.lapok(user.nev, user.old, user.ügy, user.élet, user.szerencse, user.hit, user.csapások, user.felszerelés, user.étel)


def bejel(bejnev, bejjel):
    try:
        nev = bejnev
        jelszo = bejjel
        adatjo = 0
        bejfile = open("mentes.txt", "r")
        for i in bejfile:
            szovtom = i.split("|")
            if szovtom[0] == nev and szovtom[1] == jelszo:
                adatjo = 1
                user.nev = szovtom[0]
                user.old = szovtom[2]
                user.szerencse = szovtom[3]
                user.ügy = szovtom[4]
                user.élet = szovtom[5]
                user.hit = szovtom[6]
                user.csapások = szovtom[7]
                user.felszerelés = szovtom[8]
                user.étel = szovtom[9]
        if adatjo == 1:
            print("létezik ilyen felhasználó")
            print(user.old)
            jatek.lapok(user.nev, user.old, user.ügy, user.élet, user.szerencse, user.hit, user.csapások, user.felszerelés, user.étel)
        else:
            print("nem találtam ilyen felhasználót")
    except Exception as e:
        print(e)


