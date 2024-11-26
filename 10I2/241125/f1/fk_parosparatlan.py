import os
os.system("cls")

szamok = []
f = open("szamok.sza","r",encoding="utf-8")
for row in f:
    row = row.strip()
    szam = int(row)
    szamok.append(szam)
f.close()

parosf = open("parosak.txt","w",encoding="utf-8")
paratlanf = open("paratlan.txt","w",encoding="utf-8")

for szam in szamok:
    if szam%2 == 0:
        parosf.write(f"{szam}\n")
    else:
        paratlanf.write(f"{szam}\n")

parosf.close()
paratlanf.close()