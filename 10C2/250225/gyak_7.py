import os
os.system("cls")

szamok = []
while True:
    try:
        szam = int(input("Add meg a számot: "))
    except:
        print("Nem számot adtál meg")
    else:
        if szam == 100:
            break
        szamok.append(szam)

print(f"Összeg: {sum(szamok)}")