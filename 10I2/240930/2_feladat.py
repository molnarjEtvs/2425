eletkorok = []
while True:
    eletkor = input("Add meg az életkort: ")
    eletkor = int(eletkor)
    if eletkor == 0:
        break
    else:
        eletkorok.append(eletkor)
print(eletkorok)