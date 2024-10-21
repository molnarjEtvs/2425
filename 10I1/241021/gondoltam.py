import random,os
os.system("cls")
gondoltSzam = random.randint(1,1000)
tipp = 0
while gondoltSzam != tipp:
    tipp = input("Add meg a tipped: ")
    tipp = int(tipp)
    if tipp>gondoltSzam:
        print("Kissebb számra gondoltam")
    elif tipp<gondoltSzam:
        print("Nagyobb számra gondoltam")
    else:
        print("ELTALÁLTAD!")