import os
os.system("cls")

try:
    szam = int(input("Adj meg egy egész számot"))
except:
    print("Nem számot adtál meg")
else:
    for x in range(0,szam+1):
        if x%3 == 0:
            print(x)