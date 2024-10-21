import random,os
os.system("cls")
nyeroSzamok = []
while len(nyeroSzamok)<5:
    szam = random.randint(1,90)
    if szam not in nyeroSzamok:
        nyeroSzamok.append(szam)
nyeroSzamok.sort()
print(nyeroSzamok)