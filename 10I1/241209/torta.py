class Torta:
    def __init__(self,emeletek:int,kenve:bool):
        self.emeletek = emeletek
        self.kenve = kenve

    def ujEmelet(self):
        self.emeletek += 1
    
    def kremmelMegken(self):
        if self.kenve == False:
            self.kenve = True
            return True
        else:
            return False
    
    def mennyiKaloria(self):
        kaloria = self.emeletek*1000
        if self.kenve == True:
            kaloria *= 2
        return kaloria
    
torta1 = Torta(1,False)
torta2 = Torta(1,False)
torta1.kremmelMegken()
torta1.kremmelMegken()
torta2.ujEmelet()