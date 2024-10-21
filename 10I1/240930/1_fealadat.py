db = input("Hány db zöldség: ")
db = int(db)
zoldsegek = []
for x in range(1,db+1):
    zoldseg = input(f"Add meg a(z) {x}. zöldség: ")
    zoldsegek.append(zoldseg)
print(zoldsegek)