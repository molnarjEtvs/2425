import os
os.system("cls")

kutyak = []
while True:
    nev = input("Add meg a kutya nevét: ")
    if not nev: #if nev == "":
        break
    else:
        kutya = {}
        kutya['nev'] = nev
        kutya['kaja'] = input("Add meg a kaját: ")
        kutyak.append(kutya)

print(kutyak)