import random,os
os.system("cls")
gondoltSzam = random.randint(1,1000)
fszam = 0
while fszam != gondoltSzam:
    fszam = input("Add meg a tippelt számod: ")
    fszam = int(fszam)
    if fszam>gondoltSzam:
        print("A gondolt szám kisebb")
    elif fszam<gondoltSzam:
        print("A gondolt szám nagyobb")
    else:
        print("ELTALÁLTAD!!")