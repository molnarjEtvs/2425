import os
os.system('cls')

try:
    bruttoFizetes = int(input("Add meg a bruttó fizetés: "))
    kor = int(input("Add meg az életkorod: "))
except:
    print("Nem számot írtál be")
else:
    szja = bruttoFizetes * 0.15
    if kor < 25:
        szja = 0
    tb = bruttoFizetes * 0.185
    szocho = bruttoFizetes * 0.13
    nettoFizetes = bruttoFizetes - szja - tb
    munkaltatoKoltseg = bruttoFizetes + szocho
    print(f"A fizetésedből levont SZJA összege: {szja} Ft, TB összeg: {tb} Ft\nA nettó fizetésed: {nettoFizetes} Ft\nA munkáltató ezt az összeget utalta el neked: {munkaltatoKoltseg} Ft")