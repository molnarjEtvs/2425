class Macska:
    def __init__(self,nev:str,kor:int,fajta:str):
        self.nev = nev
        self.kor = kor
        self.fajta = fajta
        self.ehseg = 50
        self.mozgasigeny = 0

    def etetes(self,mennyiseg:int):
        self.ehseg -= mennyiseg
        if self.ehseg<0:
            self.ehseg = 0
    
    def jatszas(self,ido:int):
        self.mozgasigeny -= ido
        if self.kor < 1:
            self.ehseg += ido*2
        else:
            self.ehseg += ido
    
    def alvas(self,ido:int):
        self.mozgasigeny += ido
        if ido>=8:
            self.ehseg += 5
        else:
            self.ehseg += 2

    def setallapot(self):
        if self.ehseg<20:
            self.allapot = "éhes"
        elif self.ehseg>=20 and self.ehseg<60:
            self.allapot = "éhesen járkál" 
        else:
            self.allapot = "Jól lakott"