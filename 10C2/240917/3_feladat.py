szam1 = input("Szám 1: ")
szam1 = int(szam1)
szam2 = input("Szám 2: ")
szam2 = int(szam2)

for x in range(szam1,szam2+1):
    if x%2==0:
        print(x)