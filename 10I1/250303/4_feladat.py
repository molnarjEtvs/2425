import os
os.system("cls")

betuk = []
while True:
    betu = input("Adj meg egy betűt: ")
    if betu == "Q":
        break
    betuk.append(betu.upper())

print(betuk)