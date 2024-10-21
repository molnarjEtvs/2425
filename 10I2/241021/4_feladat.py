import random, os
os.system("cls")
rszam = random.randint(1,1000)
uszam = input("Add meg a számot: ")
uszam = int(uszam)
if rszam>uszam:
    print(f"A random szám nagyobb: {rszam}")
elif rszam<uszam:
    print(f"A random szám kisebb: {rszam}")
else:
    print(f"Egyenlő: {rszam}")