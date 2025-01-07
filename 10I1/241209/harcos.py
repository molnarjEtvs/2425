import random
class Harcos:
    def __init__(self,nev:str,eletEro:int,harciEro:int):
        self.nev = nev
        self.eletEro = eletEro
        self.harciEro = harciEro

    def harcol(self,masikHarcos:object):
        self.eletEro -= masikHarcos.harciEro
        masikHarcos.eletEro -= self.harciEro
        if self.eletEro <= 0 or masikHarcos.eletEro<=0:
            return True
        else:
            return False
    
    def setEletero(self,ujErtek:int):
        self.eletEro = ujErtek

    def getEletero(self):
        return self.eletEro
    
harcos1 = Harcos("Sebestyén",random.randint(80,100),random.randint(5,10))
harcos2 = Harcos("Robi",random.randint(80,100),random.randint(5,10))
while harcos1.harcol(harcos2) == False:
    print(f"{harcos1.nev}/{harcos1.getEletero()}")
    print(f"{harcos2.nev}/{harcos2.getEletero()}")
print(f"{harcos1.nev}/{harcos1.getEletero()}")
print(f"{harcos2.nev}/{harcos2.getEletero()}")