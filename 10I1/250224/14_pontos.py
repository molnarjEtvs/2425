def hiressegRogzites():
    hiressegek  = []
    while True:
        nev = input("Add mega hiresseg nevét: ")
        if not nev:
            break
        hiressegek.append(nev.upper())
    return hiressegek

def elemzes(szemelyek:list):
    db = len(szemelyek)
    print(f"{db} db személy került rögzítésre")
    alexanderDb = 0
    for szemely in szemelyek:
        if szemely.startswith("ALEXANDER") == True:
            alexanderDb += 1
    print(f"Alexanderrel {alexanderDb} db kezdődik")
    szoveg = "<#>".join(szemelyek)
    print(f"{szoveg}")

g = hiressegRogzites()
elemzes(g)
        