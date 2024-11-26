'''
Írjunk egy eljárást amely egy bementi paraméterről kiírja, hogy pozitiv szám, negatív szám, vagy nulla. 
'''
import fuggvenyeim

x = input("adj meg egy számot: ")
x = int(x)
fuggvenyeim.megallapit(x)
fuggvenyeim.megallapit(-10)
fuggvenyeim.megallapit(0)