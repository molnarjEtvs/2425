import os
os.system("cls")

gyumolcsok = []

try:
    db = int(input("add meg a gyumolcs számát: "))
except:
    print("Nem számot adtál meg")
else:
    for _ in range(db):
        gyumolcs = input("Add meg a gyumolcsöt: ")
        gyumolcsok.append(gyumolcs.capitalize())