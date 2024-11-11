import os
os.system("cls")
szo = input("Adj meg egy szót: ")
szelesseg = input("Szélesség: ")
szelesseg = int(szelesseg)
kitolto = input("Add meg a kitöltő karaktert: ")
szoKozepen = szo.center(szelesseg,kitolto)
print(szoKozepen)