import os
os.system("cls")
gyumolcsok = []
while True:
    gyumolcs = input("Adj meg egy gyümölcs nevet: ")
    if gyumolcs == "":
        break
    else:
        gyumolcs = gyumolcs.capitalize()
        gyumolcsok.append(gyumolcs)
print(gyumolcsok)