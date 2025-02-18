import random
class LolHos:
    def __init__(self,azonosito:int, nev:str,tipus:str,stilus:int):
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
        lehetKepesseg = ["átokszórás", "végítélet", "halál", "bájolás"]
        self.kepesseg = random.choice(lehetKepesseg)


hosok = []

with open("hosok.hsk","r",encoding="utf-8") as fajl:
    for sor in fajl:
        sor = sor.strip().split("|")
        hos1 = LolHos(int(sor[0]),sor[1],sor[2],int(sor[3]))
        hos1.setNehezsegiSzint(int(sor[4]))
        hos1.setKepessegek()
        hosok.append(hos1)
        del hos1

with open("hoseim.txt","w",encoding="utf-8") as f:
    for hos in hosok:
        f.write(f"Azonosító: #{hos.azonosito}\n")
        f.write(f"Hős neve: {hos.nev}\n")
        f.write(f"Nehézségi szint: {hos.tipus}\n")
        f.write(f"Képesség: {hos.kepesseg}\n")
        f.write("#"*40)
        f.write("\n")