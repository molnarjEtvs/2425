def hiressegRogzites():
    hiressegek = []
    while True:
        hireseg = input("Add meg a híresség nevét: ")
        if not hireseg:
            break
        hiressegek.append(hireseg.upper())
    return hiressegek

def elemzes(szemelyek:list):
    db = len(szemelyek)
    print(f"{db} személy lett rögzítve")
    alexanderDb = 0
    for szemely in szemelyek:
        if szemely.startswith("ALEXANDER") == True:
            alexanderDb +=1
    print(f"Alexanderrel {alexanderDb} db kezdődik")
    szoveg = "<#>".join(szemelyek)
    print(f"Rögzített nevek: {szoveg}")

f = hiressegRogzites()
elemzes(f)