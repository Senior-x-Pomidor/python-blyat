last_update = "22.06.2025"

def clear_terminal():

    # \033[H setzt den Cursor oben links, \033[J löscht bis zum Ende
    print("\033[H\033[J", end="")

def farbig(text, farbcode):
    return f"\033[{farbcode}m{text}\033[0m"

def big_text(text):

    if text == "hangman":
        print("\033[1;31m    __  __                                            \033[0m")
        print("\033[1;31m   / / / /____ _ ____   ____ _ ____ ___   ____ _ ____ \033[0m")
        print("\033[1;33m  / /_/ // __ `// __ \ / __ `// __ `__ \ / __ `// __ \\""\033[0m")
        print("\033[1;32m / __  // /_/ // / / // /_/ // / / / / // /_/ // / / /\033[0m")
        print("\033[1;34m/_/ /_/ \__,_//_/ /_/ \__, //_/ /_/ /_/ \__,_//_/ /_/ \033[0m")
        print("\033[1;34m                     /____/                           \033[0m")
        print("by dani (Senior-x-Pomidor) "+last_update)
        print(" \n \n \n \n \n")

def game_pick_mode_hangman():

    big_text("hangman")

    print("Bitte Spielmodus auswählen:\n ")
    print(farbig("1. 1 v anyone", 32) + " mind. 1 Spieler\n---Einfach gegeneinander spielen!\n")
    print(farbig("2. Computer  ", 32) + " 1 Spieler\n---Gegen den Computer Spielen            (noch nicht verfügbar)\n")
    print(farbig("3. Exit      ", 31) + " \n---Spiel schließen\n")



    mode = 0

    while mode != 1 and mode != 2 and mode != 3:

        try:
            mode = int(input("Zahl eingeben (1-3):"))
        except:
            mode = 0
        
        if mode != 1 and mode != 2 and mode != 3:

            print("Ungültige Eingabe!")
            
    if mode == 1:
        clear_terminal()
        game_hangman_1_v_anyone()
    
    if mode == 3:
        clear_terminal()
        return