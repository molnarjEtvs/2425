import os
os.system("cls")
kajak = []
while True:
    nev = input("Add meg a nevet: ")
    if not nev:
        break
    else:
        kaja = input("Add meg a étel nevét: ")
        kutyaKaja = {}
        kutyaKaja['nev'] = nev
        kutyaKaja['kaja'] = kaja
        kajak.append(kutyaKaja)
    
print(kajak)