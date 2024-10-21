import random
bekertSzam = input("Adj meg egy számot: ")
bekertSzam = int(bekertSzam)
randomSzam = random.randint(1,1000)

if bekertSzam>randomSzam:
    print(f"A bekértszám {bekertSzam} nagyobb mint a randomszám {randomSzam}")
elif bekertSzam<randomSzam:
    print(f"A bekértszám {bekertSzam} kisebb mint a randomszám {randomSzam}")
else:
    print("A két szám egyenlő!")