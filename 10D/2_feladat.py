szoveg = input("Adj meg egy mondatot: ")

if szoveg.isalnum() == True:
    print("IGEN")
else:
    print("NEM")

print(f"{szoveg.upper()}")