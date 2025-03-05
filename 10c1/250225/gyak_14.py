import os
os.system("cls")

with open("torlesztesek.txt","w",encoding="utf-8") as fajl:
    while True:
      
            osszeg = int(input("Add meg az összeget: "))
            if osszeg == -1:
                  break
            fajl.write(f"{osszeg}\n")
            print("Fájlba írás")
