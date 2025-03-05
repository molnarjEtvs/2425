import os
os.system("cls")

try:
    zoldsegDb = int(input("Add meg a zöldésgek számát: "))
except:
    print("Nem számot adtál meg")
else:
    zoldsegek = []
    for _ in range(0,zoldsegDb+1):
        zoldseg = input("Add meg a zöldség nevét: ")
        zoldsegek.append(zoldseg.lower())
