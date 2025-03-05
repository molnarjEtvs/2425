import os
os.system("cls")

try:
    szam = int(input("Adj meg egy számot: "))
except:
    print("Nem számot adtál meg")
else:
    for i in range(0,szam+1):
        if i%3==0:
            print(i)