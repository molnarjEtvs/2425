szamok = []
stoppolo = input("add meg a stoppolot: ")
stoppolo = int(stoppolo)
while True:
    szam = input("Add meg a számot: ")
    szam = int(szam)
    if stoppolo == szam:
        break
    else:
        if szam not in szamok:
            szamok.append(szam)

print(szamok)
    