import os
os.system("cls")

try:
    aramerosseg = int(input("Add meg az áram erősséget"))
    feszultseg = int(input("Add meg a feszültséget"))
    ido = float(input("add meg az időt: "))
except:
    print("Nem számot adtál meg")
else:
    teljesitmeny = (feszultseg * aramerosseg) / 1000
    energiafogyasztas = teljesitmeny * ido
    if energiafogyasztas <= 1:
        print("Alacsony")
    elif energiafogyasztas >1 and energiafogyasztas<=5:
        print("Fokozott")
    else:
        print("Nagy")
    