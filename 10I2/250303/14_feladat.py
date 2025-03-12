
with open("torlesztesek.txt","a",encoding="utf-8") as fajl:
    while True:
        torleszto = int(input("Add meg a törlesztőrészletet: "))
        if torleszto == -1:
            break
        fajl.write(f"{torleszto}\n")
