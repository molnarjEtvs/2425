import random
class Lakas:
    def __init__(self,hom:float,szel:int,hossz:int,cim:str):
        self.hom = hom
        self.szel = szel
        self.hossz = hossz
        self.cim = cim
        self.ablakNyitva = False

    def teruletSzamolas(self):
        self.terulet = self.szel * self.hossz

    def ertekBecsles(self,m2Ar:int):
        self.ertek = self.terulet * m2Ar
    
    def szelloztetes(self,perc:int):
        self.ablakNyitva = True
        self.hom -= perc / 5

    def futes(self,perc:int):
        if self.ablakNyitva == True:
            self.ablakNyitva = False
        self.hom += perc / 3

lakasok = []

with open("lakaslista.txt","r",encoding="utf-8") as f:
    for sor in f:
        sor = sor.strip()
        adatok = sor.split(";")
        lakas1 = Lakas(float(adatok[0]),int(adatok[1]),int(adatok[2]),adatok[3])
        lakas1.teruletSzamolas()
        lakas1.ertekBecsles(random.randint(150000,320000))
        lakas1.szelloztetes(30)
        lakas1.futes(10)
        lakasok.append(lakas1)
        del lakas1


with open("lakaseredmenyek.txt","w",encoding="utf-8") as f:
    for lakas in lakasok:
        f.write(f"Cím: {lakas.cim}\n")
        f.write(f"Terület: {lakas.terulet}m2.\n")
        f.write(f"Érték: {lakas.ertek} Ft.\n")
        f.write(f"Hőmérsélet: {round(lakas.hom,2)}C.\n")
        f.write("#"*40)
        f.write("\n")    
