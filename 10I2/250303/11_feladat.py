

diak = {}
try:
    eletkor = int(input("Add meg az életkorod"))
except:
    print("Nem számot adott meg: ")
else:
    osztaly = input("Add meg az osztály: ")
    kedvencSzin = input("Add meg a kedvenc színed")
    diak['kor'] = eletkor
    diak['kedvencSzin'] = kedvencSzin
    diak['osztaly'] = osztaly
    print(f"Életkor: {diak['kor']}, Osztály: {diak['osztaly']}, Kedvenc szín: {diak['kedvencSzin']}")