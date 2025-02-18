def fagylaltNevek():
    izek = []
    while True:
        iz = input("Add meg a fagyi ízt: ")
        if not iz:
            break
        izek.append(iz.capitalize())
    return izek

def Statisztika(izek:list):
    db = len(izek)
    print(f"{db} féle fagylalt kapható.")
    veganDb = 0
    for iz in izek:
       if iz.find("vegán") >= 0 or iz.find("Vegán") >= 0:
           veganDb += 1
    print(f"Ebből vegán ízesítésű: {veganDb} db.")

x = fagylaltNevek()
Statisztika(x)