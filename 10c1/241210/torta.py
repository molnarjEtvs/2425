class Torta:
    def __init__(self,emeletSzam:int,kenve:bool):
        self.emeletSzam = emeletSzam
        self.kenve = kenve

    def ujEmelet(self):
        self.emeletSzam += 1

    def kremmelMegken(self):
        if self.kenve == False:
            self.kenve = True
            return True
        else:
            return False
        
    def mennyiKaloria(self):
        kaloria = self.emeletSzam * 1000
        if self.kenve == True:
            kaloria *= 2
        return kaloria
    
torta1 = Torta(2,False)
torta2 = Torta(1,False)
torta1.kremmelMegken()
torta1.kremmelMegken()
print(f"{torta1.emeletSzam}")
torta1.ujEmelet()
print(f"{torta1.emeletSzam}")
