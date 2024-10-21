db = input('Add meg hány db zöldésget szeretnél rögzíteni: ')
db = int(db)
zoldsegek = []
for x in range(1,db+1):
    zoldseg = input(f'Add meg a(z) {x}. zöldséget: ')
    zoldsegek.append(zoldseg)
print(zoldsegek)