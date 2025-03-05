import os
os.system("cls")

zoldsegek = []
db = int(input("Add meg a zöldségek számát: "))
for _ in range(db):
    zoldseg = input("Add meg a zöldésget: ")
    zoldsegek.append(zoldseg.lower())

