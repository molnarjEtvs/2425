import datetime
class Ember:
    def __init__(self,vezetekNev:str,keresztNev:str,szuletesiEv:int):
        self.vezetekNev = vezetekNev
        self.keresztNev = keresztNev
        self.szuletesiEv = szuletesiEv

    def hogyHivjak(self):
        return self.vezetekNev +" "+self.keresztNev
    
    def eletKor(self):
        ma = datetime.date.today() #2024-12-09
        ev = ma.year
        return ev-self.szuletesiEv

ember1 = Ember("Buga","Pista",1987)
print(f"Név: {ember1.hogyHivjak()}")
print(f"kor: {ember1.eletKor()}")