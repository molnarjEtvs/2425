def bolygoRogzites():
    bolygok = []
    while True:
        bolygo = input("Add meg a bolygó nevét: ")
        if not bolygo:
            break
        bolygok.append(bolygo.capitalize())
    return bolygok

def bolygoElemzes(bolygok:list):
    db = len(bolygok)
    print(f"Elemek száma: {db} db")
    db4 = 0
    for bolygo in bolygok:
        if len(bolygo) == 4:
            db4 += 1
    print(f"4 karakteresek: {db4} db")
    szoveg = "_$_".join(bolygok)
    print(f"{szoveg}")
b = bolygoRogzites()
bolygoElemzes(b)
