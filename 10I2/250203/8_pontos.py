import os
os.system("cls")

lolHosNev = input("Add LOL hős nevét: ")
try:
    alapero = float(input("Add meg az alaperőt: "))
except:
    print("Nem számot adtál meg: ")
else:
    sebesseg = (alapero * 0.225) + 10
    magikusEro = (alapero/2) * 0.9
    print(f"A hősöd neve: {lolHosNev.upper()}")
    print(f"Futási sebesség: {sebesseg} km/h")
    print(f"Mágikus erő: {magikusEro} Mp")