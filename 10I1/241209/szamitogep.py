class Szamitogep:
    def __init__(self,szabadTarhely:float,kapcsolva:bool,azonosito:str):
        self.szabadTarhely = szabadTarhely
        self.kapcsolva = kapcsolva
        self.azonosito = azonosito

    def kapcsol(self):
        if self.kapcsolva == False:
            self.kapcsolva = True
        else:
            self.kapcsolva = False
    
    def programMasol(self,mb:float):
        if self.kapcsolva == True and mb<self.szabadTarhely:
            self.szabadTarhely-=mb
            return True
        else:
            return False
        
szgep1 = Szamitogep(500,False,"123456")
szgep2 = Szamitogep(1000,False,"789123")

szgep1.kapcsol()
allapot = szgep1.programMasol(800)
if allapot==True:
    print("másolás sikeres")
else:
    print("Másolás sikertelen")
allapot = szgep1.programMasol(400)
if allapot==True:
    print("másolás sikeres")
else:
    print("Másolás sikertelen")
allapot = szgep2.programMasol(1)
if allapot==True:
    print("másolás sikeres")
else:
    print("Másolás sikertelen")

