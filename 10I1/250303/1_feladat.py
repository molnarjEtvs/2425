import os
os.system("cls")

try:
    szam = int(input("Adj meg egy számot: "))
except:
    print("Nem számot adtál meg")
else:
    if szam>=0 and szam<=15:
        print("Kis szám")
    elif szam>=15 and szam<=21:
        print("Közepes szám")
    elif szam>21:
        print("Nagy szám")