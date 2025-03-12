

with open("gyumolcsok.txt","w",encoding="utf-8") as fajl:
    db = int(input("Add meg a gyümölcsök számát: "))
    for _ in range(db):
        gyuminev = input("Add meg a gyümülcs nevét: ")
        fajl.write(f"{gyuminev}\n")
