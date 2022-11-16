import tkinter
from tkinter import *
from tkinter import ttk


def lapok(nev, oldal, ugy, elet, szer, hit, csap, fel):

    def nulla():
        ab = Tk()
        keret = ttk.Frame(ab)
        print("akarsz játszani? " + str(nev) + " a(z) " + str(oldal) + " oldalnál voltál")

        ab.mainloop()
    print("eljut1")

    if oldal == "nulla":
        nulla()




