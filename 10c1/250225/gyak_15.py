import os
os.system("cls")

szo = input("Add meg szót: ")
if szo.startswith("k") == True or szo.startswith("K"):
    print("A szó k-val kezdődik") 
else:
    print("A szó nem k-val kezdődik")