szam1 = input("Add meg az első számot: ")
szam1 = int(szam1)
szam2 = input("Add meg második számot: ")
szam2 = int(szam2)
for x in range(szam1, szam2+1):
    if x % 2 == 0:
        print(x)


