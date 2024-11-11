
bruttoFizetes = input("Add meg a bruttó fizetésed: ")
bruttoFizetes = int(bruttoFizetes)

eletekor = input("Add meg az életkorod: ")
eletekor = int(eletekor)

szja = bruttoFizetes * 0.15

if eletekor<25:
    szja = 0

tb = bruttoFizetes * 0.185
szocho = bruttoFizetes * 0.13

netto = bruttoFizetes - szja - tb
munkaltato = bruttoFizetes + szocho

print(f"A nettó fizetésed: {netto} Ft")
print("Levonsára kerül: ")
print(f"SZJA: {szja} Ft")
print(f"TB: {tb} Ft")
print(f"Ez a munkáltatónak {munkaltato} Ft-ba kerül!")
