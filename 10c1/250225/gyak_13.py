import os
os.system("cls")

with open("gyumolcsok.txt","w",encoding="utf-8") as fajl:
    db = int(input("add meg a gyüm számokat: "))
    for _ in range(db):
        gyumolcs = input("gyüm név: ")
        fajl.write(f"{gyumolcs}\n")