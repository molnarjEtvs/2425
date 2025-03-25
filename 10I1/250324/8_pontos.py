import os
os.system("cls")

try:
    evesFogyasztas = int(input("Add meg az éves fogyasztást: "))
    db = int(input("Add meg a mosások számát: "))
except:
    print("Nem számot adtál meg")
else:
    aramdij = 40
    if evesFogyasztas<=0 or db<=0:
        print("Sajnos ezekkel nem tudok számolni")
    else:
        aramigeny = evesFogyasztas/db
        aramKoltseg = aramigeny*aramdij
        aramKoltseg = round(aramKoltseg,2)
        print(f"Egy mosás áramköltsége: {aramKoltseg} Ft")