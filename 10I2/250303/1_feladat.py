import os
os.system("cls")

try:
    szam = int(input("Add meg egy számot: "))
except:
    print("Nem számot adtál meg")
else:
    if szam>=0 and szam<=15:
        print("Kicsi szám")
    elif szam>=16 and szam<=21:
        print("Közepes")
    elif szam>21:
        print("Nagy szám")