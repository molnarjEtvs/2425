szam = input("adj meg egy számot: ")
szam = int(szam)
for x in range(0,szam+1):
    if x % 3 == 0:
        print(x)