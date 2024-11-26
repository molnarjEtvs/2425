'''
Készíts egy programot, amely diákok neveit és osztályzatait kezeli. 
1. lépésként kérdezzük meg hogy hány darab diákot akarsz rögzíteni
- nevét mindenképpen el kell kérni
- tantárgyak rögzítése:
-->Tantrágy neve, majd utána az osztályzatot egészen addig ami a tantárgy neve üresen nem marad.

Végül írjuk ki a diákok nevét és tantrágyát az alábbi minta szerint:

'''

import os
os.system("cls")
db = input("Add meg a tanulók számát: ")
db = int(db)
diakok = []
for sorszam in range(db):
    nev = input(f"Add meg a(z) {sorszam+1}. tanuló nevét: ")
    tantargyak = []
    while True:
        tnev = input("Add meg a tantárgy nevét: ")
        if not tnev:
            break
        else:
            jegy = input("Add meg az osztályzatot: ")
            jegy = int(jegy)
            tantargy = {}
            tantargy['nev'] = tnev
            tantargy['jegy'] = jegy
            tantargyak.append(tantargy)
    diak = {}
    diak['nev'] = nev
    diak['tantargyak'] = tantargyak
    diakok.append(diak)
print(diakok)
