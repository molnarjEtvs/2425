import random,os
os.system("cls")
fszam = input("Adj meg egy számot: ")
fszam = int(fszam)
rszam = random.randint(1,1000)
if fszam>rszam:
    print(f"A felhasználó szám nagyobb! random: {rszam}")
elif fszam<rszam:
    print(f"A felhasználó szám kisebb! random: {rszam}")
else:
    print(f"A két szám egyenlő! random: {rszam}")