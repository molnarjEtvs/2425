import os
os.system("cls")

try:
    vizigeny = float(input("Add meg a vízigényt: "))
    db = int(input("Add meg a darabszámot: "))
except:
    print("Nem számot adtál meg!")
else:
    m3Dij = 218.95
    vizFogyasztas = (vizigeny*db)/1000
    vizKoltseg = m3Dij * vizFogyasztas
    if db<1000:
        vizKoltseg *= 2
    elif db>=1000 and db<2000:
        vizKoltseg *= 1.8
    else:
        vizKoltseg *= 1.5

    vizKoltseg = round(vizKoltseg,2)
    print(f"{vizFogyasztas} m3 a vízfogyasztás, ami {vizKoltseg} Ft-ba kerül. ")

