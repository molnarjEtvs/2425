import random, Fegyver
class Karakter:
    def __init__(self,nev:str):
        self.nev = nev
        self.eletPont = 25
        self.ero = 0
        self.gyorsasag = 0
        self.ugyesseg = 0
        self.fegyver = None

    def fegyverValasztas(self,fegyver:object):
        if isinstance(fegyver,self.megengedettFegyverek()):
            self.fegyver = fegyver
            print(f"{self.nev.upper()} aki egy {self.tipus} fegyvere: {fegyver.tipus}")
        else:
            print(f"{self.nev.upper()} nem választhatja a {fegyver.nev} mert ő egy {self.nev.upper()}")

    def megengedettFegyverek(self):
        return (Fegyver)
    
    def kasztValasztas(kasztSzam:int,nev:str):
        if kasztSzam == 1:
            return Karakter.Harcos(nev)
        elif kasztSzam == 2:
            return Karakter.Tolvaj(nev)
        elif kasztSzam == 3:
            return Karakter.Pap(nev)
        else:
            return False
        
    def fegyverAzonositas(fegyverSzam:int):
        if fegyverSzam == 1:
            return Fegyver.Kard()
        elif fegyverSzam == 2:
            return Fegyver.Tor()
        elif fegyverSzam == 3:
            return Fegyver.Bot()
        elif fegyverSzam == 4:
            return Fegyver.Pallos()
        elif fegyverSzam == 5:
            return Fegyver.Buzogany()
        else:
            return False

def Harcos(Karakter):
    def __init__(self,nev:str):
        super().__init__(nev)
        self.ero = random.randint(1,10)+10
        self.gyorsasag = random.randint(1,6)+random.randint(1,6)+8
        self.ugyesseg = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
        self.tipus = "Harcos"

    def megengedettFegyverek(self):
        return (Fegyver.Kard,Fegyver.Pallos,Fegyver.Buzogany)

def Tolvaj(Karakter):
    def __init__(self,nev:str):
        super().__init__(nev)
        self.ero = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
        self.gyorsasag = random.randint(1,10)+10
        self.ugyesseg = random.randint(1,6)+random.randint(1,6)+8
        self.tipus = "Tolvaj"

    def megengedettFegyverek(self):
        return (Fegyver.Kard,Fegyver.Tor)

def Pap(Karakter):
    def __init__(self,nev:str):
        super().__init__(nev)
        self.ero = random.randint(1,6)+random.randint(1,6)+8
        self.gyorsasag = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
        self.ugyesseg = random.randint(1,10)+10
        self.tipus = "Pap"

    def megengedettFegyverek(self):
        return (Fegyver.Kard,Fegyver.Bot,Fegyver.Buzogany,Fegyver.Tor)