def fagylaltNevek():
    fagylaltIzek = []
    while True:
        iz = input("Add meg a fagylalt nevét: ")
        if not iz:
            break
        fagylaltIzek.append(iz.capitalize())
    return fagylaltIzek

def Statisztika(lista:list):
    db = len(lista)
    print(f"{db} fagylalt kapható")
    veganDb=0
    for fagyi in lista:
        if fagyi.find('vegán')>-1 or fagyi.find('Vegán')>-1:
            veganDb += 1
    print(f"Ebből vegán ízesítésű: {veganDb} db")

f = fagylaltNevek()
Statisztika(f)