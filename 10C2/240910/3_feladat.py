szam = input("Adj meg egy egész számot: ")
szam = int(szam)

if szam%3 == 0 or szam%5 == 0:
    print("igen")
else:
    print("nem")