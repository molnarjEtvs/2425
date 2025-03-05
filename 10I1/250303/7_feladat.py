import os
os.system("cls")

szamok = []
while True:
    try:
        szam = int(input("Adjon meg számot"))
    except:
        print("nem szám")
    else:
        if szam == 100:
            break
        szamok.append(szam)
    
print(f"Összeg: {sum(szamok)}")