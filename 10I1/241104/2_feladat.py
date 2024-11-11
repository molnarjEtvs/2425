import os
os.system("cls")

szo = input("Adj meg egy szót: ")
szelesseg = input("Add meg a szélességet: ")
szelesseg = int(szelesseg)
karakter = input("Add meg a karaktert: ")
kozepen = szo.center(szelesseg,karakter)
print(kozepen)