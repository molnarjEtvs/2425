import os
os.system("cls")

try:
    szam = int(input("Add meg a számot: "))
except:
    print("Nem számot írtál be")
else:
    if szam>=0 and szam<=15:
        print("kicsi szám")
    elif szam>=16 and szam<=21:
        print("Közepes")
    elif szam>21:
        print("Nagy szám")