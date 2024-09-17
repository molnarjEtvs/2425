osszeg = 0
szam = 1
while szam != 0:
    szam = input("Adj meg egy számot: ")
    szam = int(szam)
    osszeg += szam
print(f"A számok összege: {osszeg}")