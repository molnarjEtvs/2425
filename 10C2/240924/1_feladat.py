db = input("Add meg a darabszámot: ")
db = int(db)
zoldsegek = []
for x in range(1,db+1):
    zoldseg = input(f"Add meg az {x}. zöldséget: ")
    zoldsegek.append(zoldseg)
print(zoldsegek)