import os
os.system("cls")
mondat = input("Adj meg egy mondatot: ")
szo = input("Add meg a szót: ")

if mondat.startswith(szo) == True:
    print(f"A mondat {szo}-val kezdődik")
elif mondat.endswith(szo) == True:
    print(f"A mondat {szo}-ra VÉGZŐDIK")
else:
    print("Egyik sem")