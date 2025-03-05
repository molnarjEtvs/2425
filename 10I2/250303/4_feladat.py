import os
os.system("cls")

betuk = []
while True:
    betu = input("Add meg a betűt: ")
    if betu == "Q":
        break
    betuk.append(betu.upper())
print(betuk)

