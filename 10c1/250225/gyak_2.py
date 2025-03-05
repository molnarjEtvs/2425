import os
os.system("cls")

szoveg = input("Add meg a szöveget: ")
if szoveg.isalnum() == True:
    print("Igen")
else:
    print("Nem")
print(f"{szoveg.upper()}")