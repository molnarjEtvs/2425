class Macska:
    def __init__(self,nev:str,kor:int,faj:str):
        self.nev = nev
        self.kor = kor
        self.faj = faj
        self.ehseg = 50
        self.mozgasIgeny = 0
    
    def etetes(self,mennyiseg:int):
        self.ehseg -= mennyiseg
        if self.ehseg<0:
            self.ehseg = 0
    
    def jatszas(self,ido:int):
        self.mozgasIgeny -= ido
        if self.kor < 1:
            self.ehseg += ido*2
        else:
            self.ehseg += ido

    def alvas(self,ido:int):
        self.mozgasIgeny += ido
        if ido >= 8:
            self.ehseg += 5
        else:
            self.ehseg += 2

