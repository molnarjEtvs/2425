import os
os.system("cls")
gyumolcsok = []
while True:
    gyumolcs = input("Add meg a gyümölcs nevét: ")
    if gyumolcs == "":
        break
    else:
        gyumolcs = gyumolcs.capitalize()
        gyumolcsok.append(gyumolcs)
print(gyumolcsok)