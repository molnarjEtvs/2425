eletekorok = []
while True:
    eletkor = input("Add meg az életkort: ")
    eletkor = int(eletkor)
    if eletkor == 0:
        break
    else:
        eletekorok.append(eletkor)
print(eletekorok)