import os
os.system("cls")

def rovidSzoKereso(szavak:list):
    legrovidebbSzo=szavak[0]
    for szo in szavak:
        if len(szo) < len(legrovidebbSzo):
            legrovidebbSzo=szo
    print(f"A legrövidebb szó: {legrovidebbSzo}")

szavak=["alma", "körte", "barack", "szőlő", "banán"]

rovidSzoKereso(szavak)