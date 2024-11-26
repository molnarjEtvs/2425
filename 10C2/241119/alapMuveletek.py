'''
Írjunk egy függvényt ami két szám alapműveletek elvégzéséért felelős (összeadás, kivonás, szorzás, osztás), és az eredménnyel tér vissza.
Bemeneti paraméter:
- Műveleti jel (+,-,*,/)
- Szám 1
- Szám 2
Figyeljünk arra, hogy 0-val nem osztunk!
'''

def muvelet(jel,szam1,szam2):
    if jel == "+":
        return szam1 + szam2
    elif jel == "-":
        return szam1 - szam2
    elif jel == "*":
        return szam1 * szam2
    elif jel == "/":
        if szam2 == 0:
            return "0-val nem osztunk!"
        return szam1 / szam2
    else:
        return "Nem ismert művelet"

x = muvelet("+",20,40)
print(x)