def szamolas(jel,szam1,szam2):
    if jel == "+":
        return szam1+szam2
    elif jel == "-":
        return szam1-szam2
    elif jel == "*":
        return szam1*szam2
    elif jel == "/":
        if szam2 == 0:
            return "0-al nem osztunk!"
        return szam1/szam2
    else:
        return "Nincs ilyen műveleti jel!"

x = szamolas("+",34,52)
print(x)