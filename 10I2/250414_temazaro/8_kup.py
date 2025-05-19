import os,math
os.system("cls")

try:
    r = int(input("Add meg a sugarat:"))
    m = int(input("Add meg a magasságot: "))
except:
    print("Nem számot adtál meg értéknek")
else:
    pi = 3.14
    V = round((r*r*pi*m)/3,2)
    a = math.sqrt(r*r+m*m)
    A = round((r*r*pi)+(r*pi*a),2)
    print(f"A felszín: {A}")
    print(f"Térfogat {V}")
    if A>=10:
        print("A felszín legalább 10")