import os
os.system("cls")

lolHos = input("Add meg a hős nevét: ")
try:
    alapEro = float(input("Add meg az alaperőt: "))
except:
    print("Nem számot adtál meg")
else:
    sebessege = (alapEro * 0.225) + 10
    magikusEro = (alapEro/2) * 0.9
    print(f"Lol hős neve: {lolHos.upper()}")
    print(f"Futási sebesség: {sebessege} km/h")
    print(f"Mágikus erő: {magikusEro} Mp")