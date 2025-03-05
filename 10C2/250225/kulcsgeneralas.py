import os
os.system("cls")

def pontosan(maxKarakter:int,szoveg:str):
    if len(szoveg) == maxKarakter:
        return True
    else:
        return False

def elso2Nagye(szoveg):
    if szoveg[0] == szoveg[0].upper() and szoveg[1] == szoveg[1].upper():
        return True
    else:
        return False

def szerepelBenne(karakter:str,szoveg:str):
    if szoveg.find(karakter) > -1:
        return True
    else:
        return False

def vanBenneLegalabbSzam(db:int,szoveg):
    talatSzam = 0
    for karakter in szoveg:
        if karakter.isdigit() == True:
            talatSzam+=1
    if talatSzam>=db:
        return True
    else:
        return False
    
def szamkarakterekSzamaParose(szoveg):
    db = 0
    for karakter in szoveg:
        if karakter.isdigit() == True:
            db+=1
    if db%2==0:
        return True
    else:
        return False

szoveg = input("Adj meg egy szöveget: ")


ellenOrzes = True
if pontosan(30,szoveg) == False:
    ellenOrzes = False
if elso2Nagye(szoveg) == False:
    ellenOrzes = False
if szerepelBenne("ß",szoveg) == False:
    ellenOrzes = False
if vanBenneLegalabbSzam(3,szoveg) == False:
    ellenOrzes = False



#végső ellenőrzés
if ellenOrzes == True:
    print("Helyes")
else:
    print("Helytelen")