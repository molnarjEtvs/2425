import random, os
os.system("cls")

lehetosegek = ["","Kő","Papír","Olló"]
ny = 0
v = 0
d = 0
for _ in range(5):
    user = input("1.Kő/2.Papír/3.Olló: ")
    user = int(user)

    gep = random.randint(1,3)

    if user == gep:
        print(f"döntetlen, mert user: {lehetosegek[user]} | gép: {lehetosegek[gep]}")
        d += 1
    elif (user == 1 and gep == 3) or (user == 2 and gep == 1) or (user == 3 and gep == 2):
        print(f"nyertél, mert user: {lehetosegek[user]} | gép: {lehetosegek[gep]}")
        ny += 1
    else:
        print(f"vesztettél, mert user: {lehetosegek[user]} | gép: {lehetosegek[gep]} ")
        v += 1

if ny>= 3:
    print("ÖSSZESÉGÉBEN NYERTÉL!")
elif d >= 3:
    print("ÖSSZESÉGÉBEN DÖNTETLEN!")
else:
    print("ÖSSZESÉGÉBEN VESZTETTÉL!")