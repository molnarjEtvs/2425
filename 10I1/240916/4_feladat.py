pontszam = input("Add meg a pontszámot: ")
pontszam = int(pontszam)

if pontszam<50:
    print("1 (elégtelen)")
elif pontszam>=50 and pontszam<60:
    print("2 (elégséges)")
elif pontszam>=60 and pontszam<70:
    print("3 (közepes)")
elif pontszam>=70 and pontszam<85:
    print("4 (jó)")
else:
    print("5 (jeles)")