
import random
valasz = input("Lebegő (l) / Egész szám (e) :")

if valasz == "l":
    szam = random.uniform(1,3000)
    print(szam)
elif valasz == "e":
    szam = random.randint(1,3000)
    print(szam)
else:
    print("Hibás választás")