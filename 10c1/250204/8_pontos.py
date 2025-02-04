try:
    gombocAr = int(input("Add meg mennyibe kerül egy gombóc: "))
    tolcserAr = int(input("Add meg mennyibe kerül egy tölcsér: "))
    gombocokSzama = int(input("Add meg hány gombocot szeretnél: "))
except:
    print("Egyik válaszra nem számot adtál")
else:
    if gombocokSzama>3:
        tolcserAr = 0
    osszeg = (gombocAr*gombocokSzama)+tolcserAr
    print(f"{gombocokSzama} gombóc fagylalt a tölcsérrel együtt {osszeg} Ft lesz.")
