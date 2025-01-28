import random
class OkosCserep:
    def __init__(self,nev:str,fenyigeny:str,vizigeny:str,ultetesiHonap:int):
        self.nev = nev
        self.fenyigeny = fenyigeny
        self.vizigeny = vizigeny
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

with open("novenyek.txt","r",encoding="utf-8") as fajl:
    for sor in fajl:
        sor = sor.strip()
        adatok = sor.split("|")
        cserep1 = OkosCserep(adatok[0],adatok[1],adatok[2],int(adatok[3]))
        cserep1.napfenySzimulacio(random.randint(10,60))
        cserep1.locsolas(random.randint(0,50))
        cserep1.tartalyToltes(50)
        cserepek.append(cserep1)
        del cserep1

with open("cserepek.txt","w",encoding="utf-8") as barmi:
    for cserep in cserepek:
        barmi.write(f"Növény: {cserep.nev}\n")
        barmi.write(f"Fényigény/Vízigény: {cserep.fenyigeny}/{cserep.vizigeny}\n")
        barmi.write(f"Ültetés hónapja: {cserep.ultetesiHonap}. hónap\n")
        barmi.write(f"Talajnedvesség: {cserep.talajNedvesseg}\n")
        barmi.write(f"Tartályszint: {cserep.tartalySzint}ml\n")
        if cserep.fenyigeny == "magas" and cserep.vizigeny == "magas":
            barmi.write("KÉNYES NÖVÉNY\n")
        barmi.write("*"*40)
        barmi.write("\n")
        
