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
        
    def futkos(self):
        self.suly -= 0.1
        if self.ehese == False:
            self.ehese = True
    
    def jelenlegiErtekek(self):
        print(f"Macska neve: {self.nev}")
        print(f"Súly: {self.suly} kg")
        if self.ehese == True:
            print("ÉHES")
        else:
            print("NEM éhes")


cica1 = Macska("Zsolt",3.5,True)
cica2 = Macska("Károly",5.0,False)

cica1.jelenlegiErtekek()
cica2.jelenlegiErtekek()

for _ in range(10):
    cica2.futkos()

cica2.jelenlegiErtekek()