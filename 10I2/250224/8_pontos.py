import os
os.system("cls")
try:
    aramerrosseg = int(input("Add meg az áram erősséget: "))
    feszultseg = int(input("Add meg a feszültséget: "))
    ido = float(input("Add meg az időt: "))
except:
    print("Nem számokat adtál meg")
else:
    teljesitmeny = (feszultseg * aramerrosseg) / 1000
    energiafogyasztas = teljesitmeny * ido
    if energiafogyasztas<=1:
        print("Alacsony Energiafogyasztás")
    elif energiafogyasztas>1 and energiafogyasztas<=5:
        print("Fokozott")
    else:
        print("Nagy")
    