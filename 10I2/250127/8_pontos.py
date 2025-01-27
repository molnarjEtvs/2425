import os
os.system("cls")

#vizigeny = input("Add meg a vízigény: ")
#vizigeny = float(vizigeny)

try:
    vizigeny = float(input("Add meg a vízigényt"))
    darabszam = int(input("Add meg a darabszámot: "))
    m3Dij = 218.95
    vizfogyasztas = (vizigeny*darabszam)/1000
    vizKoltseg = m3Dij*vizfogyasztas
    if darabszam<1000:
        vizKoltseg *= 2
    elif darabszam>=1000 and darabszam<2000:
        vizKoltseg *= 1.8
    else:
        vizKoltseg *= 1.5
    
    vizKoltseg = round(vizKoltseg,2)
    print(f"{vizfogyasztas} m3 a vízfogyasztás, ami {vizKoltseg} Ft-ba kerül.")

except:
    print("Rossz formátumot adtál meg!")
