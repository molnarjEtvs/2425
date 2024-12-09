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
        #self.suly = self.suly-0.1
        if self.ehese == False:
            self.ehese = True

    def jelenlegiErtekek(self):
        print(f"Macska neve: {self.nev}")
        print(f"Macska súlya: {self.suly} kg")
        if self.ehese == True:
            print("ÉHES")
        else:
            print("NEM éhes")

macska1 = Macska("Cirmi",2.1,True)
macska2 = Macska("Garfield",5.4,False)
macska2.eszik(0.5)
macska1.futkos()
macska1.jelenlegiErtekek()