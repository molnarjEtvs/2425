import random,os
os.system("cls")
vszam = random.randint(1,1000)
tip = 0
while vszam != tip:
    tip = input("Add meg a tipped: ")
    tip = int(tip)
    if tip<vszam:
        print("A gondolt szám nagyobb")
    else:
        print("A gondolt szám kisebb")
print("ELTALÁLTAD!")