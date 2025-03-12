import random
class Karakter:
    def __init__(self,nev:str):
        self.nev = nev
        self.eletPont = 25
        self.ero = 0
        self.gyorsasag = 0
        self.ugyesseg = 0
        self.fegyver = None
        self.kepesseg = None


class Harcos(Karakter):
    def __init__(self,nev:str):
        super().__init__(nev)
        self.ero = random.randint(1,10)+10
        self.gyorsasag = random.randint(1,6)+random.randint(1,6)+8
        self.ugyesseg = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
        self.tipus = "Harcos"

class Tolvaj(Karakter):
    def __init__(self,nev:str):
        super().__init__(nev)
        self.ero = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
        self.gyorsasag = random.randint(1,10)+10
        self.ugyesseg = random.randint(1,6)+random.randint(1,6)+8
        self.tipus = "Tolvaj"

class Pap(Karakter):
    def __init__(self,nev:str):
        super().__init__(nev)
        self.ero = random.randint(1,6)+random.randint(1,6)+8
        self.gyorsasag = random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
        self.ugyesseg = random.randint(1,10)+10
        self.tipus = "Pap"