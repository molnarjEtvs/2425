import os
os.system("cls")

szamok = []
while True:
    try:
        szam = int(input("Adj meg egy számot: "))
    except:
        print("nem egész számot adtál meg")
    else:
        if szam == 100:
            break
        szamok.append(szam)

print(f"{sum(szamok)}")