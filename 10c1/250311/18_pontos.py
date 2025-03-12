import random
class Lakas:
    def __init__(self,homerseklet:float,szelesseg:int,hosszusag:int,cim:str):
        self.homerseklet = homerseklet
        self.szelesseg = szelesseg
        self.hosszusag = hosszusag
        self.cim = cim
        self.ablakNyitva = False

    def teruletSzamolas(self):
        self.terulet = self.szelesseg * self.hosszusag    
    
    def ertekBecsles(self,m2Ar:int):
        self.ertek = self.terulet * m2Ar

    def szelloztetes(self,perc:int):
        self.ablakNyitva = True
        self.homerseklet -= perc/5

    def futes(self,perc:int):
        if self.ablakNyitva == True:
            self.ablakNyitva = False
        self.homerseklet += perc/3

lakasok = []


with open("lakaslista.txt","r",encoding="utf-8") as fajl:
    for sor in fajl:
        sor = sor.strip().split(";")
        lakas1 = Lakas(float(sor[0]),int(sor[1]),int(sor[2]),sor[3])
        lakas1.teruletSzamolas()
        lakas1.ertekBecsles(random.randint(150000,320000))
        lakas1.szelloztetes(30)
        lakas1.futes(10)
        lakasok.append(lakas1)
        del lakas1

with open("lakaseredmenyek.txt","w",encoding="utf-8") as fajl:
    for lakas in lakasok:
        fajl.write(f"Cím: {lakas.cim}\n")
        fajl.write(f"Terület: {lakas.terulet}m2\n")
        fajl.write(f"Érték: {lakas.ertek} Ft\n")
        fajl.write(f"Hőmérsélet: {round(lakas.homerseklet,2)}C\n")
        fajl.write("#"*20)
        fajl.write("\n")
