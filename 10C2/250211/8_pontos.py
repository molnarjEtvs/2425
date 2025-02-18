
try:
    gombocAr = int(input("Add meg mennyibe kerül egy gombóc fagylalt: "))
    tolcserAr = int(input("Add meg mennyibe kerül egy tölcsér: "))
    gombocDb = int(input("Add meg a gombócok számát: "))
except:
    print("Valamelyikre nem számot adtál meg!")
else:
    if gombocDb>3:
        tolcserAr = 0
    fizetendo = (gombocAr*gombocDb) + tolcserAr
    print(f"{gombocDb} gombóc fagylalt a tölcsérrel együtt {fizetendo} Ft lesz.")