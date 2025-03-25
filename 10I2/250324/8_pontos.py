import os
os.system("cls")

try:
    kw = int(input("Add meg az éves fogyasztást: "))
    db = int(input("Add meg a mosások számát: "))
except:
    print("Nem számot adtál meg")
else:
    aramdij = 40
    if kw == 0 or db == 0:
        print("Sajnos 0-val nem lehet számolni")
    else:
        aramigeny = kw/db
        aramKoltseg = round((aramigeny*aramdij),2)
        print(f"Egy mosás áramköltsége: {aramKoltseg} Ft")

