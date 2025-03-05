import os
os.system("cls")

allat = {}
allat["tipus"] = "házi"
allat["emlos"] = "igen"
try:
    labak = int(input("Add meg a lábak számát: "))
except:
    print("Nem számot adtál meg")
else:
    allat["labak"] = labak
    print(f"Típus: {allat['tipus']}, Emlős: {allat['emlos']}, Lábak száma: {allat["labak"]}")