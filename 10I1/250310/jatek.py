import Karakter,Fegyver,random,os
os.system("cls")

jatekosok = []
for jatekosSzama in range(2):
    nev = input(f"Add meg a(z) {jatekosSzama+1} karakter nevét: ")
    while True:
        karakterSzam = int(input("Melyik karaktert választod?\n1.Harcos\n2.Tolvaj\n3.Pap\nVálasztásod: "))
        if karakterSzam in range(1,4):
            break
    
