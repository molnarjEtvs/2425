import os
os.system("cls")

kor = input("Add meg a macska korát: ")
kor = int(kor)

suly = input("Add meg a macska súlyát: ")
suly = float(suly)

adag = 65

mennyiseg = suly*adag*7

if kor<2:
    kcal = 80
elif kor>=2 and kor<5:
    kcal = 95
else:
    kcal = 110

mozgasigeny = suly*kcal

print(f"A macska heti étel szükséglete: {mennyiseg} g")
print(f"A macska napi mozgásigénye: {mozgasigeny} kcal")