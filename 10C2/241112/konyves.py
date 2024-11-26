'''
Írj egy programot, amelyben könyvek adatait (szerző, cím, oldalszám) tudja rögzíteni a felhasználó. A könyvek adatainak tárolására használjon a program szótárakat, amelyek egy lista elemei legyenek! Az adatbekérés addig folytatódjon, amíg a felhasználó a szerző megadásakor nem gépel be adatot, csupán ENTER-t üt! A program ekkor listázza ki a már bevitt adatokat, és fejezze be a működését!
'''
import os
os.system("cls")
konyvek = []
while True:
    cim = input("Add meg a könyv címét: ")
    if not cim:
        break
    else:
        konyv = {}
        konyv['cim'] = cim
        konyv['szerzo'] = input("Add meg a könyv szerzőjét: ")
        oldalszam = input("Add meg az oldalszámot: ")
        oldalszam = int(oldalszam)
        konyv['oldalszam'] = oldalszam
        konyvek.append(konyv)

print(konyvek)