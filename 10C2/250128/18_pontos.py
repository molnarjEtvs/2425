import random
class OkosCserep:
    def __init__(self,nev:str,fenyIgeny:str,vizIgeny:str,ultetesHonapja:int):
        self.nev = nev
        self.fenyIgeny = fenyIgeny
        self.vizIgeny = vizIgeny
        self.ultetesHonapja = ultetesHonapja
        self.talajNedvesseg = 0
        self.tartalySzint = 100
    
    def napfenySzimulacio(self,ido:int):
        self.talajNedvesseg -= ido/2
        if self.talajNedvesseg < 0:
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


with open("cserepek.txt","w",encoding="utf-8") as csf:
    for cserep in cserepek:
        csf.write(f"Növény: {cserep.nev}\n")
        csf.write(f"Fényigény/Vízigény: {cserep.fenyIgeny}/{cserep.vizIgeny}\n")
        csf.write(f"Ültetés hónapja: {cserep.ultetesHonapja}\n")
        csf.write(f"Talajnedvesség: {cserep.talajNedvesseg}\n")
        csf.write(f"Tartályszint: {cserep.tartalySzint}\n")
        if cserep.fenyIgeny == "magas" and cserep.vizIgeny == "magas":
            csf.write("KÉNYES NÖVÉNY\n")
        csf.write("*"*30)
        csf.write("\n")
        
