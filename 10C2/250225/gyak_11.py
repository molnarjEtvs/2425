import os
os.system("cls")

diak = {}

try:
    diak_eletkor = int(input("Add meg az életkorod: "))
except:
    print("Nem számot adtál meg:")
else:
    kedvenc_szin = input("Add meg a kedvenc színed: ")
    osztaly = input("Add meg az osztályod: ")
    diak['eletkor'] = diak_eletkor
    diak['szin'] = kedvenc_szin
    diak['osztaly'] = osztaly
    print(f"Életkor: {diak['eletkor']}, Osztály: {diak['osztaly']}, Kedvenc szín: {diak['szin']}")