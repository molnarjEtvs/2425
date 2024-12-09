class Harcos:
    def __init__(self,nev:str,eletEro:int,harciEro:int):
        self.nev = nev
        self.eletEro = eletEro
        self.harciEro = harciEro

    def harcol(self,masikHarcos:object):
        self.eletEro -= masikHarcos.harciEro
        masikHarcos.eletEro -= self.harciEro
        print(f"harcos1: {self.eletEro}")
        print(f"harcos2: {masikHarcos.eletEro}")
        if self.eletEro <= 0 or masikHarcos.eletEro<=0:
            return True
        else:
            return False
        
    def getEletEro(self):
        return self.eletEro
    
    def setEletEro(self,ertek:int):
        self.eletEro = ertek


harcos1 = Harcos("Magyar Péter",100,8)
harcos2 = Harcos("Orbán Viktor",150,3)

while(harcos1.harcol(harcos2) == False):
    print(f"{harcos1.eletEro}")
    print(f"{harcos2.eletEro}")

