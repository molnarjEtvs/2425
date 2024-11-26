'''
Írj egy programot, amelyben könyvek adatait (szerző, cím, oldalszám) tudja rögzíteni a felhasználó. A könyvek adatainak tárolására használjon a program szótárakat, amelyek egy lista elemei legyenek! Az adatbekérés addig folytatódjon, amíg a felhasználó a szerző megadásakor nem gépel be adatot, csupán ENTER-t üt! A program ekkor listázza ki a már bevitt adatokat, és fejezze be a működését!'''
import os
os.system("cls")

konyvek = []
while True:
    szerzo = input("Add meg a szerzőt: ")
    if not szerzo:
        break
    else:
        konyv = {}
        konyv['szerzo'] = szerzo
        konyv['cim'] = input("Add meg a könyv címét: ")
        oldalszam = input("Add meg az oldal számot: ")
        oldalszam = int(oldalszam)
        konyv['oldalszam'] = oldalszam
        konyvek.append(konyv)

print(konyvek)