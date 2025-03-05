import os
os.system("cls")

zoldsegek = []

try:
    db = int(input("add meg a zöldésgek száma: "))
except:
    print("Nem számot adtál meg")
else:
    for _ in range(db):
        zoldseg = input("Add meg a zöldésget: ")
        zoldsegek.append(zoldseg.lower())

