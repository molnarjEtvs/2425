szo = input("Adj meg egy szót: ")
db = input("add meg hányszot írjam ki: ")
db = int(db)
for sorszam in range(1,db+1):
    print(f"{sorszam}. {szo}")
