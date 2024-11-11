import os
os.system("cls")
parosak = []
paratlanok = []
oszthatokHarommal = []
for x in range(1,101):
    if x%2 == 0:
        parosak.append(x)
    else:
        paratlanok.append(x)
    
    if x%3==0:
        oszthatokHarommal.append(x)

print(f"Páros számok: {parosak}")
print(f"Páratlanok számok: {paratlanok}")
print(f"3-al oszthatók számok: {oszthatokHarommal}")
