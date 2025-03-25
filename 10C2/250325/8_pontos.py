import os
os.system("cls")

try:
    evesFogyasztas = int(input("adja meg az éves fogyasztást: "))
    mosasokSzama = int(input("add meg a mosások számát: "))
except:
    print("Nem számot írtál be")
else:
    aramdij = 40
    if evesFogyasztas <= 0 or mosasokSzama <= 0:
        print("Sajnos ezekkel az adatokkal nem tudok számolni")
    else:
        aramIgyeny = evesFogyasztas/mosasokSzama
        aramKoltseg = aramIgyeny*aramdij
        aramKoltseg = round(aramKoltseg,2)
        print(f"Egy mosás áramköltsége: {aramKoltseg} Ft")
