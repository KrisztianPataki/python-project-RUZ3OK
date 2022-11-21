import tkinter
from tkinter import *
from tkinter import ttk

#fejezet minta:
#def fejnév():
#ab = TK()
#frame = ttk.frame
#ab.title fejezetnév
#ttk.Label(ab), text="szöveg", font=méret).grid(coll, row)
#ttk gombok
# ab.mainloop()


def lapok(nev, oldal, ugy, elet, szer, hit, csap, fel, étel):

    ab = Tk()

    def karlap():

        karab = Tk()
        karab.title("karakterlap")
        karab.minsize(width=200, height=200)
        karframe = ttk.Frame(karab)



        ttk.Label(karab, text=nev, font=25).grid(column=0, row=1)
        ttk.Label(karab, text="életpontok: "+str(elet), font=20, foreground="red").grid(column=0, row=2)

        ttk.Label(karab, text="ügyesség: " + str(ugy), font=20).grid(column=0, row=3)

        ttk.Label(karab, text="szerencse: " + str(szer), font=20).grid(column=0, row=4)

        ttk.Label(karab, text="hit: " + str(hit), font=20).grid(column=0, row=5)
        ttk.Button(karab, text="mi ez?", command="").grid(column=1, row=5)

        ttk.Label(karab, text="étel: " + str(étel), font=20).grid(column=0, row=9)
        ttk.Button(karab, text="mire jó?", command="").grid(row=9, column=2)

        ttk.Label(karab, text="felszerelés: " + fel, font=20).grid(column=0, row=10)
        ttk.Label(karab, text="csapások: " + csap, font=20).grid(column=0, row=11)
        ttk.Button(karab, text="bezár", command=karab.destroy).grid(column=4, row=13)
        karab.mainloop()

    def nulla():

        frame = ttk.Frame(ab)
        ab.title("bevezető")

        ttk.Label(ab, text="""
                                                Háttértörténet
A hatalmas vagyonokról és kincsekről szóló pletykák csalogattak el Femphrey nyugati szegletéből
Mautistatia veszedelmes földjére, a hósipkás mászhatalan hegyek otthonába, melyek mindent elrejtő,
fagyos ködbe burkolóznak.A levegő hideg,nyirkos te is csak a vastag prémkapátnak köszönheted hogy nem vacogsz.
A dülöngélő szekérben kushadva azon töprengsz, miközben északra, Mortvania felé haladsz, hogy van-e a szóbeszédnek bármi alapja.
Az emberek, akikkel eddig találkoztál, mind soványak és rongyos göncöket hordanak — nem pont így képzelted el ezt az állítólag gazdag vidéket!
De talán a kincsek el vannak rejtve valahová, és a helyiek csak nem találtak még rá. . .
Gondolataidból hangos csikorgás hangja ráz fel, amint a szekér megáll. A kocsis kinyitja az ajtót, és leemeli csomagjaidat a tetőről.
Szürke alkonyatba lépsz ki, téli köd ereszkedik a falura, Leverhelvenre, ahol a mai éjszakára megszállsz.
A fogadó kicsi, és a legnagyobb jóindulattal sem lehet fényűzőnek nevezni, azonban az étel forró, a forralt bor pedig erős és frissítő.
A helyiek viszont, akik jól láthatóan nem bíznak az idegenekben, keveset beszélnek. Miután belépsz a fogadóba,
az ajtót elreteszelik, az ablakokon végignézve pedig megállapítod, hogy azokat már korábban eltorlaszolták.
Különös hely ez, és a neve is furcsa: a Szívére — márpedig a fogadtatás a legnagyobb jóindulattal sem nevezhető szívből jövőnek.
Meg is kérded a fogadóst, honnan jött az elnevezés, mire azonnal halotti csönd települ a nagyteremre.
A férfi elfordul, és minden igyekezeted ellenére sem hajIandó hozzád szólni. Eltöprengsz rajta,
hogy egy ilyen udvarias és ártalmatlan kérdés hogyan válthat ki ilyen ellenséges reakciót az emberekből.
Egy másik fickó, aki a kandalló mellett ül, még a lábad elé is köp!
Egy idős, sálakba és kezeslábasba Öltözött asszony alaposan végigmér. — Ezek a külhoniak nem tudják, mikor kell csöndben maradniuk.
— Egy pohár itallal felszerelkezve leülsz a nő mellé — Ő legalább beszél hozzád, ami sokkal több, mint amit a többiekről el lehet mondani.
Mohón inni kezd. — Az nem „Szívére”, idegen. Sose hívták így, csak a cégért változtatták meg. Ez a „Szív Vére,” így, külön írva. Ez az, amit oly sokan adtak fel itt, a szívük vérét!
Az időközben feléledt halk mormogás megint megszűnik. Többen is dühös pillantással mérnek végig titeket, a pultos pedig rákiált a nőre, hogy hallgasson.
A melegtől és a bortól pirospozsgás arcú asszony azonban nem hagyja, hogy belefojtsák a szót. — A Gróf az,
az istenit a fekete szívébe. Falusiak tűnnek el, és többé soha nem látjuk őket. A Gróf viszi el őket a kastélyába, ahol szörnyű halált halnak. Szörnyűt! Többen is hallották
éjszakánként a sikolyokat, a pokolban senyvedő lelkek segélykiáltásait. — Ekkor már könnycseppek csorognak meggyötört arcáról. — Hát nem tegnap ragadta el a kisunokámat?
Hát nem tegnap láttuk a hintóját és a fej nélküli lovast a faluban? Szegény kis Nastassiámat, azt a gyönyörű, szőke, kedves kislányt elragadta az a bestia, és egyetlen igazi,
bátor férfi sincs ebben az isten háta mögötti porfészekben, aki elég bátor lenne ahhoz, hogy a kastélyba menjen, és megmentse!
Kínos motyogások hangzanak fel innen-onnan, miközben a kandallóban szikrák pattognak; az égő fa ropogása szinte nyomatékosítja az öregasszony kétségbeesett segélykérését:
— Könyörgöm, jó uram, mentse meg őt. Még csak tizenhét, soha nem ártott Ő senkinek. — A nő ismét zokogni kezd.
Egy magas, vörös hajú férfi áll fel az egyik asztal mellól, és hozzád lép. Látod, hogy csak egy karja van, tunikájának jobb ujja a mellkasára van tűzve.
— Messziről jött kalandozónak tűnsz, idegen. Amit az öreg Svetlana mond, igaz: a Gróf valóban szörnyű, gonosz lélek, és Heydrich kastélya tele van rémségekkel.
En magam mennék oda, hogy végezzek vele, de ezt nyilvánvalóan nem tehetem meg. — Bólintasz, amint a férfi az üres ujj felé tekint. — Segítesz rajtunk?
Harcos napjaimból maradt még néhány aranyam, amitől szívesen megválok, ha megszabadítasz minket az átokfajzattól.  Mindenki szeme esdeklően szegeződik rád.
Már epp beleegyezően bólintanál, amikor a fogadó ajtaja kicsapódik. Az emberek ijedten felsikoltanak, ahogy jeges fuvallat csap be a terembe.
Odakinn, a ködben egy fekete hintó körvonalait veszed ki, ami előtt négy éjfekete mén áll, prüszkölve és toporogva. Az ajtóban kísérteties alak 
magasodik. Csontos ujjait felemeli, és maga felé hív! De nem szól semmit — hogyan is szólhatna? Hiszen nincs feje...
                                                                ÉS MOST LAPOZZ!

        
        """, font=20).grid(column=2, row=0)

        ttk.Button(ab, text="karakterlap", command=karlap).grid(column=1, row=2, ipadx=25, ipady=25)
        ttk.Button(ab, text="LAPOZOK!", command="").grid(column=3, row=2, ipady=25, ipadx=25)
        ab.mainloop()

    if oldal == "nulla":
        nulla()




