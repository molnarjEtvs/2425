import random
class lolHos:
    def __init__(self,azonosito:int,nev:str,tipus:str,stilus:int):
        self.azonosito = azonosito
        self.nev = nev
        self.tipus = tipus
        self.stilus = stilus
    
    def setNehezsegiSzint(self,nehezsegiFok:int):
        if nehezsegiFok == 1:
            self.nsz =  "Easy"
        elif nehezsegiFok == 2:
            self.nsz = "Medium"
        else:
            self.nsz = "Hard"
    
    def setKepessegek(self):
        ertekek = ["átokszórás","végítélet","halál","bájolás"]
        self.kepesseg = random.choice(ertekek)

hosok = []

with open("hosok.hsk","r",encoding="utf-8") as fajl:
    for sor in fajl:
        sor = sor.strip() #1|Aatrox|Warrior|3|2|P
        adatok = sor.split("|") #1|Aatrox|Warrior|3|2|P
        lolhos1 = lolHos(int(adatok[0]),adatok[1],adatok[2],int(adatok[3]))
        lolhos1.setNehezsegiSzint(int(adatok[4]))
        lolhos1.setKepessegek()
        hosok.append(lolhos1)
        del lolhos1

with open("hoseim.txt","w",encoding="utf-8") as f:
    for egy in hosok:
        f.write(f"Azonosító: {egy.azonosito}\n")
        f.write(f"Hős neve: {egy.nev}\n")
        f.write(f"Nehézségi szint: {egy.nsz}\n")
        f.write(f"Képesség: {egy.kepesseg}\n")
        f.write("#"*35)
        f.write("\n")


adatok = {}
adatok['nev'] = input("Add meg nevet: ")