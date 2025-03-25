import os
os.system("cls")

try:
    fogyasztas = int(input("Add meg az éves fogyasztást: "))
    db = int(input("Add meg a mosások számát: "))
except:
    print("Nem számot adtál meg")
else:
    aramdij = 40
    if fogyasztas <= 0 or db<=0:
        print("Sajnos ezekkel nem tudunk számolni")
    else:
        aramIgeny = fogyasztas/db
        aramKoltseg = aramIgeny*aramdij
        aramKoltseg = round(aramKoltseg,2)
        print(f"Egy mosás áramköltsége: {aramKoltseg} Ft")