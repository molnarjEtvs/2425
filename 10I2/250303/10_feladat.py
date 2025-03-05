import os
os.system("cls")

allat = {}
allat['tipus'] = "Házi"
allat['emlos'] = "Igen"
try:
    labakSzam = int(input("Add meg a lábak számát: "))
except:
    print("nem szám")
else:
    allat['labakSzama'] = labakSzam
    print(f"Típus: {allat['tipus']}, Emlős: {allat['emlos']}, Lábak száma: {allat['labakSzama']} ")

