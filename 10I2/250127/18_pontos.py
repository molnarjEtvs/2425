import random
class OkosCserep:
    def __init__(self,nev:str,fenyIgeny:str,vizIgeny:str,ultetesiHonap:int):
        self.nev = nev
        self.fenyIgeny = fenyIgeny
        self.vizIgeny = vizIgeny
        self.ultetesiHonap = ultetesiHonap
        self.talajNedvesseg = 0
        self.tartalySzint = 100
    
    def napfenySzimulacio(self,ido:int):
        self.talajNedvesseg -= ido/2
        if self.talajNedvesseg<0:
            self.talajNedvesseg = 0
    
    def locsolas(self,mennyiseg:int):
        self.talajNedvesseg += mennyiseg
        self.tartalySzint -= mennyiseg

    def tartalyToltes(self,mennyiseg:int):
        if (self.tartalySzint + mennyiseg) > 500:
            self.tartalySzint = 500
            return True
        else:
            self.tartalySzint += mennyiseg
            return False


cserepek = []

with open("novenyek.txt","r",encoding="utf-8") as f:
    for sor in f:
        sor = sor.strip()
        adatok = sor.split("|")
        okos1 = OkosCserep(adatok[0],adatok[1],adatok[2],int(adatok[3]))
        okos1.napfenySzimulacio(random.randint(10,60))
        okos1.locsolas(random.randint(0,50))
        okos1.tartalyToltes(50)
        cserepek.append(okos1)
        del okos1

with open("cserepek.txt","w",encoding="utf-8") as fajl:
    for cserep in cserepek:
        fajl.write(f"Növény: {cserep.nev}\n")
        fajl.write(f"Fényigény/Vízigény: {cserep.vizIgeny}\n")
        fajl.write(f"Ültetés hónapja: {cserep.ultetesiHonap}. hónap\n")
        fajl.write(f"Talajnedvesség: {cserep.talajNedvesseg}%\n")
        fajl.write(f"Tartályszint: {cserep.tartalySzint} ml\n")
        if cserep.fenyIgeny == "magas" and cserep.vizIgeny == "magas":
            fajl.write("KÉNYES NÖVÉNY!\n")
        fajl.write("****************************\n")