import random,os
os.system("cls")
nevek = []
while True:
    nev = input("Add meg a nevet: ")
    if nev == "":
        break
    else:
        nevek.append(nev)
vnev = random.choice(nevek)
print(vnev)