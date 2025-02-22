# Maak een functie tic_tac_toe(), die ons hele hoofdprogramma bevat
from startcode.tictactoe.mytictactoe import *

def tic_tac_toe():
    bord = initialiseer_bord()
    huidige_speler = 'X'
    einde_spel = False
    winnaar = " "
    zetten = 0
    while not einde_spel:
        print_bord(bord)
        rij = int(input("welke rij? (0, 1, 2)"))
        kolom = int(input("welke kolom? (0, 1, 2)"))

        bord = zet(bord, huidige_speler, rij, kolom)

        if controleer_winnaar(bord) == True:
            print(f"{huidige_speler} heeft gewonnen")

        if huidige_speler == 'X':
            huidige_speler = 'O'
        else:
            huidige_speler = 'X'

tic_tac_toe()