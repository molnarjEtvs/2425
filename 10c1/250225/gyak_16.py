import os
os.system("cls")

szoveg = input("Add meg a márkaneveket vesszővel elválasztva:")
markanevek = szoveg.split(",")
print(f"{markanevek[1]}, {markanevek[3]}")