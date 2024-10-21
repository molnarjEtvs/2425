import random,os
os.system("cls")
lehetosegek = ["","Kő","Papír","Olló"]
for _ in range(5):
    gep = random.randint(1,3)
    user = input("1.Kő/2.Papír/3.Olló: ")
    user = int(user)
    #mikor nyer a user?
    if (user==1 and gep==3) or (user==2 and gep==1) or (user==3 and gep==2):
        print(f"NYERTÉL! gép:{lehetosegek[gep]} | user:{lehetosegek[user]}")
    elif user==gep:
        print(f"DÖNTETLEN gép:{lehetosegek[gep]} | user:{lehetosegek[user]}")
    else:
        print(f"VESZTETTÉL! gép:{lehetosegek[gep]} | user:{lehetosegek[user]}")