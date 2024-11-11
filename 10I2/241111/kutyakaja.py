import os
os.system("cls")
kutyakajak = []
while True:
    nev = input("Add meg a kutya nevét: ")
    if not nev:
        break
    else:
        kaja = input("Add meg a kaját: ")
        kutyakaja = {}
        kutyakaja['nev'] = nev
        kutyakaja['kaja'] = kaja
        kutyakajak.append(kutyakaja)
print(kutyakajak)
        