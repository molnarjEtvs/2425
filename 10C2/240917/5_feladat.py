szam = 1
osszeg = 0
while szam != 0:
    szam = input("szám: ")
    szam = int(szam)
    osszeg += szam
print(f"Összeg: {osszeg}")

#v2
while True:
    szam = input("szám: ")
    szam = int(szam)
    if szam == 0:
        break
    osszeg += szam
print(f"Összeg: {osszeg}")