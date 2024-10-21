import random,os
os.system("cls")
tanulok = []
while True:
    tanulo = input("Add meg a tanuló nevét: ")
    if tanulo == "":
        break
    else:
        tanulok.append(tanulo)
kivalaszt = random.choice(tanulok)
print(f"A felelő: {kivalaszt}")