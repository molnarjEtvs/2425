lszamok = []
while True:
    lszam = input("Adj meg egy lebegőpontos számot: ")
    lszam = float(lszam)
    if lszam in lszamok:
        break
    else:
        lszamok.append(lszam)
print(lszamok)