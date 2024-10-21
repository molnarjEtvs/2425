stoppolo = input("Add meg a stoppolót: ")
stoppolo = int(stoppolo)
szamok = []
while True:
    szam = input("Add meg a számot: ")
    szam = int(szam)
    if stoppolo == szam:
        break
    else:
        if szam not in szamok:
            szamok.append(szam)

print(szamok)