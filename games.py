last_update = "27.06.2025"

from games_and_tools import battleship
from games_and_tools import tic_tac_toe
from games_and_tools import hangman
from games_and_tools import animation_why
from games_and_tools import game2048
from games_and_tools import blackjack
from games_and_tools import googol

def clear_terminal():
    # \033[H setzt den Cursor oben links, \033[J löscht bis zum Ende
    print("\033[H\033[J", end="")

def farbig(text, farbcode):
    return f"\033[{farbcode}m{text}\033[0m"

def big_text(text):


    if text == "games":

        print("\033[1;31m   ______                             \033[0m")
        print("\033[1;31m  / ____/____ _ ____ ___   ___   _____\033[0m")
        print("\033[1;33m / / __ / __ `// __ `__ \\ / _ \\ / ___/\033[0m")
        print("\033[1;32m/ /_/ // /_/ // / / / / //  __/(__  ) \033[0m")
        print("\033[1;34m\\____/ \\__,_//_/ /_/ /_/ \\___//____/  \033[0m")
        print("\033[1;34m                                      \033[0m")
        print("by dani (Senior-x-Pomidor) "+last_update)
        print("contributed by: boris (BorisG0)")
        print("  \n \n \n \n")

def games_start():

    clear_terminal()

    big_text("games")
    

    print("Willkommen zu einer erlesenen Auswahl an Klassikern!\n\n" \
    "- Alle Spiele laufen ohne Installation zusätzlicher Bibliotheken.\n" \
    "- Für beste Darstellung Terminal auf ganzem Bildschirm anzeigen.\n" \
    "- Zum terminieren des Programms kann jederzeit Ctrl+C gedrückt werden.\n" \
    "- Bitte nicht " + "!@#*()_+{ }|$%^&: <> ? [ ] \\;', ./" +" genau so eingeben!\n\n" \
    "Derzeit verfügbare Spiele sind:\n\n")
    print(farbig("- 1.    ", 32) + "Schiffe_Versenken\n")
    print(farbig("- 2.    ", 32) + "Galgenmännchen\n")
    print(farbig("- 3.    ", 32) + "Tic-Tac-Toe\n")
    print(farbig("- 4.    ", 32) + "Blackjack\n")
    print(farbig("- 2048. ", 32) + "2048\n")
    print()
    print("Nummer des Spiels eingeben (Zahl von"+ farbig(" 1-2048", 32) +") oder"+ farbig(" Exit ", 31) + "eintippen zum beenden:")

    game = 0

    while game != 1 and game != 2 and game != 3 and game != 4 and game != 2048 and game != "Exit":

        game = input("Eingabe:")

        secret = r"""!@#*()_+{ }|$%^&: <> ? [ ] \;', ./"""

        if game == secret:
            animation_why.anim_1()
            clear_terminal()
            games_start()

        try:
            game = int(game)
        except:
            game = game
        
        if game != 1 and game != 2 and game != 3 and game != 4 and game != 2048 and game != "Exit":

            print("Ungültige Eingabe!")
            
    if game == 1:
        clear_terminal()
        battleship.game_pick_mode_battleship()

    if game ==2:
        clear_terminal()
        hangman.game_pick_mode_hangman()
    
    if game == 3:
        clear_terminal()
        tic_tac_toe.game_pick_mode_tic_tac_toe()

    if game == 4:
        clear_terminal()
        blackjack.blackjack_loop()

    if game == 2048:
        print('starting')
        game2048.start()

    if game == "Exit":
        clear_terminal()
        print(farbig("\n" +"Exit", 31) + "\n")
        return "Exit"
    

#Game start:

g = "notExit"

while g != "Exit":

    g = games_start()






