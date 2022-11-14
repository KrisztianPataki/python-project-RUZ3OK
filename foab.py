import tkinter
from tkinter import *
from tkinter import ttk
import felkez

main = Tk()

keret = ttk.Frame(main)

main.title("kaland játék kockázat")
main.minsize(width="200", height="150")
keret.grid()


def magyarazo():
    szoveg = Toplevel(main)
    szoveg.title("leírás")
    szoveg.minsize(width=200, height="200")
    Label(szoveg, text="""Ebben a programban egy kaland játék kockázat könyv egy fejezetét tudod végigjátszani.
    
    Mi a Kaland Játék Kockázat? Egy könyv alapú szöveges kalandjáték úgynevezett lapozgatós könyv
    
    Hogyan fog működni a program? A regisztrálást követően a program generál neked egy karaktert amit a karakterem gombbal meg is tudsz tekinteni, aztán az első oldalnál kezdi a könyvet. 
    Bejelentkezésnél az elmentett állásodnál folytatja a könyvet.
    
    A program ki fogja írni neked az aktuális oldal szövegét és az elérhető opciókat.
    
    
    Felhasznált mű: A vámpír Kriptája
    Eredeti név: Vault of the Vampire
    Írta: Keith Martin
    fordította: Jester
    """).pack()


ttk.Label(keret, text="Kaland Játék Kockázat").grid(column=0, row=0)
ttk.Button(keret, text="hogyan működök?", command=magyarazo).grid(column=1, row=0)

#regisztrálás
ttk.Label(keret, text="kérlek csinállj egy felhasználót").grid(column=0, row=1)

ttk.Label(keret, text="felhasználónév").grid(column=0, row=2)
regnev = ttk.Entry(keret)
regnev.grid(column=1, row=2)

ttk.Label(keret, text="jelszó").grid(column=0, row=3)
regjelszo = ttk.Entry(keret)
regjelszo.grid(column=1, row=3)
ttk.Button(keret, text="regisztrálok", command=lambda: felkez.regisztral(regnev.get(), regjelszo.get())).grid(row=4, column=1)

#felhasználó beléptetés

ttk.Label(keret, text="már van felhasználód? jelentkezz be").grid(column=3, row=1)

ttk.Label(keret, text="felhasználónév").grid(column=3, row=2)
bejnev = ttk.Entry(keret)
bejnev.grid(column=4, row=2)

ttk.Label(keret, text="jelszó").grid(column=3, row=3)
bejjel = ttk.Entry(keret)
bejjel.grid(column=4, row=3)

ttk.Button(keret, text="bejelentkezés", command=lambda: felkez.bejel(bejnev.get(), bejjel.get())).grid(column=4, row=4)


ttk.Button(keret, text="kilép", command=main.destroy).grid(column=2, row=5)

main.mainloop()
