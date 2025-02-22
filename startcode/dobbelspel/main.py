# Plaats hierin de main-functie
from startcode.dobbelspel.dobbelspel import *
print("welkom bij de casino, ")

while True:
    dobbel()
    a = input("Wil je opnieuw spelen? ")
    if a == 'ja' or a == 'Ja':
        print("Ok, opnieuw spelen!")
    elif a == 'nee' or a == 'Nee':
        break