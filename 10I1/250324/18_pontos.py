import random
class Mosogep:
    def __init__(self,marka:str,kapacitas:float,kw:float):
        self.marka = marka
        self.kapacitas = kapacitas
        self.kw = kw
        self.allapot = False
        self.energiafogyasztas = 0
    
    def bekapcsolas(self):
        if self.allapot == False:
            self.allapot = True

    def mosas(self,ido:int):
        if self.allapot == True:
            self.energiafogyasztas += ido/100*self.kw
            return True
        else:
            return False
        
    def centrifugalas(self,fordulatszam:int):
        if fordulatszam<=800:
            self.energiafogyasztas += 2
        else:
            self.energiafogyasztas += 3
    
mosogepek = []
fordulatszamok = [800,1000,1200]

with open("mosogepek.txt", "r", encoding="utf-8") as f:
    for sor in f:
        sor = sor.strip().split(";")
        mosogep1 = Mosogep(sor[0],float(sor[1]),float(sor[2]))
        mosogep1.bekapcsolas()
        mosogep1.mosas(random.randint(80,150))
        mosogep1.centrifugalas(random.choice(fordulatszamok))
        mosogepek.append(mosogep1)
        del mosogep1

with open("mosasok.txt","w",encoding="utf-8") as r:
    for mosogep in mosogepek:
        r.write(f"Márka: Bosch\n")
        r.write(f"Energia: {mosogep.kw} kw\n")
        r.write(f"Kapacitás: {mosogep.kapacitas} kg\n")
        r.write(f"Energia fogyasztás: {mosogep.energiafogyasztas} kw\n")
        if mosogep.energiafogyasztas>4:
            r.write(f"MAGAS ENERGIAFELHASZNÁLÁS!\n")
        r.write(f"------------------------------------\n")
        