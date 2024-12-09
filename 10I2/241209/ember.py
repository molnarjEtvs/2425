import datetime
class Ember:
    def __init__(self,vezetekNev:str,keresztNev:str,szuletesiEv:int):
        self.vezetekNev = vezetekNev
        self.keresztNev = keresztNev
        self.szuletesiEv = szuletesiEv
    
    def hogyHivjak(self):
        return self.vezetekNev+" "+self.keresztNev
    
    def eletkor(self):
        maiNap = datetime.date.today()
        ev = maiNap.year
        return ev-self.szuletesiEv

ember1 = Ember("Buga","Gerzsonka",1999)
print(f"{ember1.hogyHivjak()}")
print(f"Életkor: {ember1.eletkor()}")