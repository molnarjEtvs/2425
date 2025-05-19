import random
class Pokemon:
    def __init__(self,dex:int,nev:str,ero:float):
        self.dex = dex
        self.nev = nev
        self.ero = ero

    def beallitas(self):
        self.ugrasi_magassag = self.ero * 3 * 0.885
    
    def kepessegValasztas(self):
        kepessegek = ["párolgás", "tűzhányás", "lövés", "gurulás"]
        self.kepesseg = random.choice(kepessegek)
    
    def csoportositas(self,kor:int):
        if kor>=15:
            self.csoport = "Idős"
        else:
            self.csoport = "Fiatal"

pokemonok = []
with open("pokemonLista.txt","r",encoding="utf-8") as fajl:
    for sor in fajl:
        sor = sor.strip().split(",")
        pokemon1 = Pokemon(int(sor[0]),sor[1],float(sor[3]))
        pokemon1.beallitas()
        pokemon1.kepessegValasztas()
        pokemon1.csoportositas(random.randint(1,10))
        pokemonok.append(pokemon1)
        del pokemon1

with open("pokemonAdatok.txt","w",encoding="utf-8") as f:
    for pokemon in pokemonok:
        f.write(f"DEX: {pokemon.dex}\n")
        f.write(f"Név: {pokemon.nev}\n")
        f.write(f"Erő/Ugrási magasság: {pokemon.ero}/{pokemon.ugrasi_magassag} m\n")
        f.write(f"Képesség / Csoport: {pokemon.kepesseg}/{pokemon.csoport}\n")
        f.write("*"*50+"\n")