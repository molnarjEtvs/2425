import os, random
os.system("cls")

def jelszoGeneralas(hosz:int):
    abc="qwertzuiopőúsdfgjkláűíyxcvmQWERTIOŐÚASDFGJKKLŰÍYCVBM@€$ß#012346789"
    abcLista=list(abc)
    jelszo = random.sample(abcLista,hosz)
    jelszoSzoveg = "".join(jelszo)
    return jelszoSzoveg

db = int(input("Add meg a jelszó hosszát: "))
x = jelszoGeneralas(db)
print(x)