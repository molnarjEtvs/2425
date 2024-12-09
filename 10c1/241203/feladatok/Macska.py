class Macska:
    def __init__(self,nev:str,suly:float,ehese:bool):
        self.nev = nev
        self.suly = suly
        self.ehese = ehese
    
    def eszik(self,etelMennyiseg:float):
        if self.ehese == True:
            self.suly += etelMennyiseg
            self.ehese = False
            return True
        else:
            return False
        
    def futokos(self):
        self.suly -= 0.1
        if self.ehese == False:
            self.ehese = True

    def jelenlegiErtekek(self):
        print(f"Név: {self.nev}")
        print(f"Súly {self.suly} kg")
        if self.ehese == True:
            print("ÉHES")
        else:
            print("NEM éhes")

cica1 = Macska("Sanyi",3.5,True)
cica1.eszik(0.8)
for _ in range(3):
    cica1.futokos()
cica1.jelenlegiErtekek()

cica2 = Macska("Cili",6.0,True)
