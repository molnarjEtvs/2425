import os
os.system("cls")


allat = {}
allat['tipus'] = "Házi"
allat['emlos'] = "igen"
try:
    labakSzam = int(input("Lábak száma: "))
except:
    print("nem számot adtál meg")
else:
    allat['labakszama'] = labakSzam
    print(f"Típus: {allat['tipus']}, Emlős: {allat['emlos']}, Lábak száma: {allat['labakszama']}")