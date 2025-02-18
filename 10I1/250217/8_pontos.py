try:
    gombocAr = int(input("Add meg a gombóc árát: "))
    tolcser = int(input("Add meg a tölcsér árát:  "))
    gombcokSzama = int(input("Gombocok száma: "))
except:
    print("Nem számot adtál meg valahol")
else:
    if gombcokSzama>3:
        tolcser = 0
    ar = (gombcokSzama*gombocAr) + tolcser
    print(f"{gombcokSzama} gombóc fagylalt a tölcsérrel együtt {ar} Ft lesz")