import os
os.system("cls")
try:

    magassag = int(input("Add meg a magasságod (cm): "))
    suly = float(input("Add meg a súlyod (kg): "))
except:
    print("Rossz értéket adtál meg!")
else:
    magassagm=magassag/100

    tti= suly/(magassagm*magassagm)
    tti=round(tti,2)
    print(f"A te testtömeg indexed: {tti}")

    if tti < 16:
        print("Súlyos soványság")
    elif tti >= 16 and tti <=16.99:
        print("Mérsékelten sovány")
    elif tti >= 17 and tti <=18.49:
        print("Enyhe soványság")
    elif tti >= 18.5 and tti <=24.99:
        print("Normális testsúly")
    elif tti >= 25 and tti <=29.99:
        print("Túlsúlyos")
    elif tti >=30 and tti <=34.99:
        print("I. fokú elhízás")
    elif tti >=35 and tti <=39.99:
        print("II. fokú elhízás")
    elif tti >= 40:
        print("III. fókú (sulyos) elhízás")
    else:
        print("Nem tudom értelmezni az adatot")


