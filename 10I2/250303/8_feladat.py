import os, random
os.system("cls")

szamok = []
for _ in range(9):
    szam = random.randint(333,888)
    szamok.append(szam)

print(f"Összeg: {sum(szamok)}")