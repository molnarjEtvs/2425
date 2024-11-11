import os
os.system("cls")

mondat = input("Add meg a mondatot: ")
szo = input("Add meg a szót: ")

if mondat.startswith(szo) == True:
    print(f"A mondat a {szo}-val kezdődik")
elif mondat.endswith(szo) == True:
    print(f"A mondat a {szo}-ra VÉGZŐDIK")
else:
    print("Egyik sem")