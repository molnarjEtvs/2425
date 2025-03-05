import os
os.system("cls")

diak = {}
diak["eletkor"] = int(input("Add meg az életkorod"))
diak["osztaly"] = input("Add meg az osztály: ")
diak["szin"] = input("Add meg a kedvenc színed: ")

print(f"Életkor: {diak['eletkor']}, Osztály: {diak['osztaly']}, Kedvenc szín: {diak['szin']}")