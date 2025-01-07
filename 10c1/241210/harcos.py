import random
class Harcos:
    def __init__(self,nev:str,eletEro:int,harciEro:int):
        self.nev = nev
        self.eletEro = eletEro
        self.harciEro = harciEro

    def harcol(self,masikHarcos:object):
        self.eletEro -= masikHarcos.harciEro
        masikHarcos.eletEro -= self.harciEro
        if self.eletEro < 0 or masikHarcos.eletEro<0:
            return True
        else:
            return False
        
    
    def setEletero(self,ujErtek):
        self.eletEro = ujErtek

    def getEletEro(self):
        return self.eletEro
    

harcos1 = Harcos("Jani",random.randint(70,100),random.randint(10,15))
harcos2 = Harcos("Kajli",random.randint(70,100),random.randint(10,15))

while harcos1.harcol(harcos2) == False:
    print(f"{harcos1.nev}/HP:{harcos1.getEletEro()}")
    print(f"{harcos2.nev}/HP:{harcos2.getEletEro()}")

if harcos1.getEletEro()<harcos2.getEletEro():
    print(f"Nyert: {harcos2.nev}")
elif harcos1.getEletEro()>harcos2.getEletEro():
    print(f"Nyert: {harcos1.nev}")
else:
    print(f"DÖNTETLEN")