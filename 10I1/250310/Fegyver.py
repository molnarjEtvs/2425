import random
class Fegyver:
    def __init__(self,tipus:str):
        self.tipus = tipus
        self.sebzes = 0
        self.sebesseg = 0
        self.vedekezes = 0
        self.tamadas = 0

class Kard(Fegyver):
    def __init__(self):
        super().__init__("Kard")
        self.sebzes = random.randint(1,6)+3
        self.sebesseg = 6
        self.vedekezes = 8
        self.tamadas = 6

class Tor(Fegyver):
    def __init__(self):
        super().__init__("Tor")
        self.sebzes = random.randint(1,6)
        self.sebesseg = 10
        self.vedekezes = 3
        self.tamadas = 10

class Bot(Fegyver):
    def __init__(self):
        super().__init__("Bot")
        self.sebzes = random.randint(1,4)
        self.sebesseg = 8
        self.vedekezes = 10
        self.tamadas = 8

class Pallos(Fegyver):
    def __init__(self):
        super().__init__("Pallos")
        self.sebzes = random.randint(1,6)
        self.sebesseg = 1
        self.vedekezes = 1
        self.tamadas = 4

class Buzogany(Fegyver):
    def __init__(self):
        super().__init__("Buzogany")
        self.sebzes = random.randint(1,4)+2
        self.sebesseg = 4
        self.vedekezes = 5
        self.tamadas = 4