
with open("gyumolcsok.txt","w",encoding="utf-8") as fajl:
    db = int(input("Add meg a gyümölcsök számát: "))
    for _ in range(db):
        gyumolcs = input("Add meg a gyümölcsöt: ")
        fajl.write(f"{gyumolcs}\n")

