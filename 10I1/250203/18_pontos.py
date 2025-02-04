import random
class lolHos:
    def __init__(self,azonosito:int,nev:str,tipus:str,stilus:int):
        self.azonosito = azonosito
        self.nev = nev
        self.tipus = tipus
        self.stilus = stilus

    def setNehezsegiSzint(self,nehezsegiFok:int):
        if nehezsegiFok == 1:
            self.nsz = "Easy"
        elif nehezsegiFok == 2:
            self.nsz = "Medium"
        else:
            self.nsz = "Hard"
    
    def setKepessegek(self):
        lehetosegek = ["átokszórás","végítélet","halál","bájolás"]
        self.kepesseg = random.choice(lehetosegek)

hosok = []

with open("hosok.hsk","r",encoding="utf-8") as fajl:
    for sor in fajl:
        sor = sor.strip() #1|Aatrox|Warrior|3|2|P
        adatok = sor.split("|")
        hos1 = lolHos(int(adatok[0]),adatok[1],adatok[2],int(adatok[3]))
        hos1.setNehezsegiSzint(int(adatok[4]))
        hos1.setKepessegek()
        hosok.append(hos1)
        del hos1

with open("hoseim.txt","w",encoding="utf-8") as fajl2:
    for hos in hosok:
        fajl2.write(f"Azonosító: #{hos.azonosito}\n")
        fajl2.write(f"Hős neve: {hos.nev}\n")
        fajl2.write(f"Nehézségi szint: {hos.nsz}\n")
        fajl2.write(f"Képesség: {hos.kepesseg}\n")
        fajl2.write("#"*30)
        fajl2.write("\n")
