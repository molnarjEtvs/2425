import os
os.system("cls")

szoveg = input("Adj meg egy szöveget: ")
if szoveg.isalnum() == True:
    print("Igen")
else:
    print("Nem")
print(f"{szoveg.upper()}")
