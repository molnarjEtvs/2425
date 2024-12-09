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
        print(f"{self.nev}")
        print(f"{self.suly}kg")
        if self.ehese == True:
            print(f"{self.nev} nevű macsak ÉHES")
        else:
            print(f"{self.nev} nevű macsak NEM éhes")

macska1 = Macska("Garfield",5,True)
macska2 = Macska("Cirmi",2,False)

macska1.futkos()
macska1.eszik(0.5)
macska1.jelenlegiErtekek()

macska2.eszik()
        
    