try:
    gombocAr = int(input("Adja meg a gombóc árát: "))
    tolcserAr = int(input("Adja meg a tölcsér árát: "))
    gombocDb = int(input("Hány gombóc fagyit kérsz: "))
except:
    print("Nem számot adtál meg!")
else:
    if gombocDb>3:
        tolcserAr = 0

    fizetendo = (gombocAr*gombocDb)+tolcserAr
    print(f"{gombocDb} gombóc fagylalt a tölcsérrel együtt {fizetendo} Ft lesz.")