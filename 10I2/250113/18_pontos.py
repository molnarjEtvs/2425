import os,random
os.system("cls")

class Macska:
    def __init__(self,nev:str,kor:int,fajta:str):
        self.nev = nev
        self.kor = kor
        self.fajta = fajta
        self.ehseg = 50
        self.mozgasIgeny = 0

    def etetes(self,mennyiseg:int):
        self.ehseg -= mennyiseg
        if self.ehseg<0:
            self.ehseg = 0

    def jatszas(self,ido:int):
        self.mozgasIgeny -= ido
        if self.kor<1:
            self.ehseg += ido*2
        else:
            self.ehseg += ido

    def alvas(self,ido:int):
        self.mozgasIgeny += ido
        if ido >= 8:
            self.ehseg += 5
        else:
            self.ehseg += 2

    def setallapot(self):
        if self.ehseg<20:
            self.allapot = "éhes"
        elif self.ehseg>=20 and self.ehseg<60:
            self.allapot = "éhesen járkál"
        else:
            self.allapot = "jól lakott"

macskak = []


with open("macskak.txt","r",encoding="utf-8") as f:
    for sor in f:
        sor = sor.strip()
        adatok = sor.split(",")
        nev = adatok[0]
        kor = int(adatok[1])
        fajta = adatok[2]
        macska1 = Macska(nev,kor,fajta)
        macska1.jatszas(random.randint(5,10))
        macska1.etetes(random.randint(1,5))
        macska1.alvas(random.randint(5,10))
        macska1.setallapot()
        macskak.append(macska1)
        del macska1

#f = open("macskak.txt","r",encoding="utf-8")

#f.close()

with open("keszmacskak.txt","w",encoding="utf-8") as i:
    for egyMacska in macskak:
        i.write(f"Név: {egyMacska.nev}\n")
        i.write(f"Kor: {egyMacska.kor} éves\n")
        i.write(f"Fajta: {egyMacska.fajta}\n")
        i.write(f"Mozgasigény/Éhségállapot: {egyMacska.mozgasIgeny}/{egyMacska.ehseg}\n")
        i.write(f"Pillanatnyi állapot: {egyMacska.allapot}\n")
        i.write(">>>>>>>>>>>>>>>>>>>>>\n")
        
        