import os
os.system("cls")

try:
    brutto = int(input("Add meg a bruttó fizetését: "))
    eletkor = int(input("Add meg az életkort: "))
except:
    print("Nem számokat adtál meg")
else:
    szja = brutto * 0.15
    if eletkor<25:
        szja = 0
    tb = brutto * 0.185
    szocho = brutto * 0.13
    netto = brutto - szja - tb
    munkaltatoKtsg = brutto + szocho
    print(f"A fizetésedből levont SZJA összege: {szja} Ft, TB összeg: {tb} Ft\nA nettó fizetésed: {netto} Ft\nA munkáltató ezt az összeget utalta el neked: {munkaltatoKtsg} Ft")