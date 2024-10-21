szam = 1
osszeg = 0
while szam != 0:
    szam = input("Add meg a számot: ")
    szam = int(szam)
    osszeg += szam
print(f"Számok összege: {osszeg}")
