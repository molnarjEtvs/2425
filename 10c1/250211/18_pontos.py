class Ajto:
    def __init__(self,tipus:str,szin:str):
        self.tipus = tipus
        self.szin = szin
        self.nmAr = 6000

    def meretBeallit(self,szelesseg:int, magassag:int):
        self.szelesseg = szelesseg
        self.magassag = magassag

    def arSzamolas(self):
        self.ajtoAr = (self.szelesseg/100) * (self.magassag/100) * self.nmAr

ajtok = []

with open("ajtok.lst","r",encoding="utf-8") as fajl:
    for sor in fajl:
        sor = sor.strip()
        adatok = sor.split(";")
        ajto1 = Ajto(adatok[0],adatok[1])
        ajto1.meretBeallit(int(adatok[3]),int(adatok[2]))
        ajto1.arSzamolas()
        ajtok.append(ajto1)
        del ajto1

with open("arajanlat.txt","w",encoding="utf-8") as w:
    for ajto in ajtok:
        w.write(f"Ajtó típusa: {ajto.tipus}\n")
        w.write(f"Ajtó ára: {ajto.ajtoAr} Ft\n")
        w.write(f"Méret: {ajto.szelesseg}(sz)x{ajto.magassag}(m) cm\n")
        w.write("-"*30)
        w.write("\n")
