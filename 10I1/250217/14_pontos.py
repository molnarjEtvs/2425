def fagylaltNevek():
    fagyizek = []
    while True:
        nev = input("Kérem a fagyi nevét: ")
        if not nev:
            break
        fagyizek.append(nev.capitalize())
    return fagyizek

def Statisztka(fagyik:list):
    db = len(fagyik)
    print(f"{db} féle fagylalt kapható")
    veganFagyik = 0
    for fagyi in fagyik:
        if fagyi.find("vegán") > -1 or fagyi.find("Vegán") > -1:
            veganFagyik += 1
    print(f"Ebből vegán ízesítésű: {veganFagyik} db.")

ertek = fagylaltNevek()
Statisztka(ertek)