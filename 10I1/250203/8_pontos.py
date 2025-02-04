import os
os.system("cls")

karakter = input("Adj meg egy hős nevet: ")
try:
    alapero = float(input("Add meg az erőt: "))
except:
    print("Nem számot adtál meg: ")
else:
    sebesseg = (alapero*0.225) + 10
    magikusEro = (alapero/2)*0.9
    print(f"A hősöd neve: {karakter.upper()}")
    print(f"Futási sebesség: {sebesseg} km/h")
    print(f"Mágikus erő: {magikusEro} Mp")

