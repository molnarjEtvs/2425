import random
class Suti:
    def __init__(self,nev:str,tipus:str,ar:int,egyseg:str):
        self.nev = nev
        self.tipus = tipus
        self.ar = ar
        self.egyseg = egyseg
        self.eladas = 0
        self.bevetel = 0

    def EladasGeneralas(self):
        return random.randint(100,500)
    
    def BevetelSzamitas(self):
        self.bevetel = self.eladas * self.ar


sutemenyek = []

with open("cuki.txt","r",encoding="utf-8") as fajl:
    for sor in fajl:
        sor = sor.strip()
        adatok = sor.split(";")
        suti1 = Suti(adatok[0],adatok[1],int(adatok[2]),adatok[3])
        suti1.eladas = suti1.EladasGeneralas()
        suti1.BevetelSzamitas()
        sutemenyek.append(suti1)
        del suti1


with open("sutik.txt","w",encoding="utf-8") as f:
    for suti in sutemenyek:
        f.write(f"Sütemény neve: {suti.nev}\n")
        f.write(f"A sütemény kiszerelése: {suti.egyseg}\n")
        f.write(f"Eladott mennyiség: {suti.eladas}  {suti.egyseg}\n")
        f.write(f"Bevétel:  {suti.bevetel} Ft\n")
        if suti.bevetel>150000:
            f.write("NÉPSZERŰ\n")
        f.write("-"*40)
        f.write("\n")