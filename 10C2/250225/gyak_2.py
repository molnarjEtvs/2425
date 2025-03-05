import os
os.system("cls")

szoveg = input("Adj meg egy szöveget: ")
if szoveg.isalnum() == True:
    print("igen")
else:
    print("nem")

print(f"{szoveg.upper()}")