stopSzam = input("Add meg a stoppoló számot: ")
stopSzam = int(stopSzam)
szamok = []
while True:
    szam = input("Adj meg egy számot: ")
    szam = int(szam)
    if stopSzam == szam:
        break
    else:
        if szam not in szamok:
            szamok.append(szam)
print(szamok)