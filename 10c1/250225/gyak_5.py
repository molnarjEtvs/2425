import os
os.system("cls")

zoldsegek = []
try:
    darab = int(input("Add meg a zöldségek számát: "))
except:
    print("nem sázmot adtál meg")
else:
    for x in range(darab):
        zoldseg = input("Add meg a zödség nevét:")
        zoldsegek.append(zoldseg.lower())

