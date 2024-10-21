import random
nevek = []
for _ in range(5):
    nev = input("Adj meg egy nevet: ")
    nevek.append(nev)
kivalsztott = random.choice(nevek)
print(f"véletlen kiválasztva: {kivalsztott}")