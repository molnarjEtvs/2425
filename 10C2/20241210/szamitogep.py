class Szamitogep:
    def __init__(self,szabadTarhely:float,bekapcsolva:bool,az:str):
        self.szabadTarhely = szabadTarhely
        self.bekapcsolva = bekapcsolva
        self.az = az
    
    def kapcsol(self):
        if self.bekapcsolva == False:
            self.bekapcsolva = True
        else:
            self.bekapcsolva = False
    
    def programMasol(self,meret:float):
        if self.bekapcsolva == True and self.szabadTarhely>meret:
            self.szabadTarhely -= meret
            return True
        else:
            return False
        
szamitogep1 = Szamitogep(800,False,"123456")
szamitogep2 = Szamitogep(400,False,"654321")
szamitogep1.kapcsol()
if(szamitogep1.programMasol(799) == True):
    print("Másolás sikeres")
else:
    print("SIKERTELEN MÁSOLÁS")
if(szamitogep1.programMasol(400) == True):    
    print("Másolás sikeres")
else:
    print("SIKERTELEN MÁSOLÁS")