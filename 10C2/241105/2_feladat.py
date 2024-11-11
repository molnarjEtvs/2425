import os
os.system("cls")

szo = input("Adj meg egy szót: ")
szel = input("Add meg a szélességet: ")
szel = int(szel)
kitoltoKarakter = input("Adj meg egy karaktert: ")
print(szo.center(szel,kitoltoKarakter))