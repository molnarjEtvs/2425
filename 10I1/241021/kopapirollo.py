import random,os
os.system("cls")
lehetosegek = ["","Kő","Papír","Olló"]
nyeresekSzama = 0
for _ in range(5):
    tipp = input("1.Kő/2.Papír/3.Olló: ")
    tipp = int(tipp)
    gep = random.randint(1,3)
    if tipp == gep:
        print("DÖNTETLEN")
    elif (tipp == 1 and gep == 3) or (tipp == 2 and gep == 1) or (tipp == 3 and gep == 2):
        print("NYERTÉL!")
        nyeresekSzama += 1
    else:
        print("VESZTETTÉL!")
    print(f"User: {lehetosegek[tipp]} | GÉP: {lehetosegek[gep]}")

if nyeresekSzama>=3:
    print("ABSZOLÚT NYERTÉL")
else:
    print("ABSZOLÚT DÖNTETLEN/VESZTETTÉL")