import os
os.system("cls")
try:
    aramerosseg = int(input("Add meg az áramerősséget: "))
    feszultseg = int(input("Add meg a feszültséget: "))
    ido = float(input("Add meg mennyi időt használod: "))
except:
    print("Nem megfelelő számot adtál meg: ")
else:
    teljesitmeny = (feszultseg*aramerosseg)/1000
    energiafogyasztas = teljesitmeny*ido

    print(f"Az eszköz teljesítménye: {teljesitmeny} kw")
    print(f"Az eszköz energiafogyasztása: {energiafogyasztas} kwh")
    if energiafogyasztas<=1:
        print("Alacsony energiafogyasztás történt")
    elif energiafogyasztas>1 and energiafogyasztas<=5:
        print("Fokozott energiafogyasztás")
    else:
        print("NAGY energiafogyasztás")
    


