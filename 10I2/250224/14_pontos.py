def hiressegRogzites():
    hiressegek = []
    while True:
        nev = input("Add meg a híresség nevét:")
        if not nev:
            break
        hiressegek.append(nev.upper())
    return hiressegek

def elemzes(szemelyek:list):
    db = len(szemelyek)
    print(f"{db}db eleme van.")
    alexanderDb = 0
    for szemely in szemelyek:
        if szemely.startswith('ALEXANDER') == True:
            alexanderDb += 1
    print(f"Alexanderrel {alexanderDb} db kezdődik")
    szep = "<#>"
    szoveg = szep.join(szemelyek)
    print(f"Rögzítet neve: {szoveg}")

g = hiressegRogzites()
elemzes(g)

