last_update = "22.06.2025"

hangman_pictures =['''
          
          
          
          
          
          
          
          
          
          ''','''
     ┌      
     │      
     │      
     │      
     │      
     │      
     │      
     │      
  ───┴───   
 /       \ ''','''
     ┌─────┐
     │      
     │      
     │      
     │      
     │      
     │      
     │      
  ───┴───   
 /       \ ''','''
     ┌─────┐
     │     │
     │      
     │      
     │      
     │      
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │     O
     │      
     │      
     │      
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │     O
     │     |
     │     |
     │      
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │     O
     │    /|
     │     |
     │      
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │     O
     │    /|\\
     │     |
     │      
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │     O
     │    /|\\
     │     |
     │    / 
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │     O
     │    /|\\
     │     |
     │    / \\
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │    (O
     │    /|\\
     │     |
     │    / \\
     │      
     │      
  ───┴───   
 /       \ ''','''
     ┌─────┐
     │     │
     │    (O)
     │    /|\\
     │     |
     │    / \\
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │    (O)
     │   _/|\\
     │     |
     │    / \\
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │    (O)
     │   _/|\_
     │     |
     │    / \\
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │    (x)
     │   _/|\_
     │     |
     │    / \\
     │      
     │      
  ───┴───   
 /       \  ''','''
     ┌─────┐
     │     │
     │    (x)
     │   _/|\_
     │     |
     │    / \\
     │   GAME
     │   OVER
  ───┴───   
 /       \  ''']

def clear_terminal():

    # \033[H setzt den Cursor oben links, \033[J löscht bis zum Ende
    print("\033[H\033[J", end="")

def farbig(text, farbcode):
    return f"\033[{farbcode}m{text}\033[0m"

def big_text(text):

    x = -5

    if text == "hangman":
        print("\033[1;31m    __  __                                            \033[0m"+" "*(10-x) + "\033[1;37m      ,%%%%%%%%,\033[0m")
        print("\033[1;31m   / / / /____ _ ____   ____ _ ____ ___   ____ _ ____ \033[0m"+" "*(10-x) + "\033[1;37m     %%o%%/%%%%%%\033[0m")
        print("\033[1;33m  / /_/ // __ `// __ \ / __ `// __ `__ \ / __ `// __ \\""\033[0m"+" "*(10-x) + "\033[1;37m    %%%%\%%%<%%%%%\033[0m")
        print("\033[1;32m / __  // /_/ // / / // /_/ // / / / / // /_/ // / / /\033[0m"+" "*(10-x) + "\033[1;37m    %%>%%%/%%%%o%%\033[0m")
        print("\033[1;34m/_/ /_/ \__,_//_/ /_/ \__, //_/ /_/ /_/ \__,_//_/ /_/ \033[0m"+" "*(10-x) + "\033[1;37m    %%%%%o%%\%%//%\033[0m")
        print("\033[1;34m                     /____/                           \033[0m"+" "*(10-x) + "\033[1;37m    %\o%\%%/%o/%%'\033[0m")
        print("by dani (Senior-x-Pomidor) "+last_update+" "*(26-x) + "\033[1;37m      '%%\ `%/%%%'\033[0m")
        print(" "*(63-x)+"\033[1;37m        '%| |%|%'\033[0m")
        print(" "*(63-x)+"\033[1;37m          | | (O\033[0m")
        print(" "*(63-x)+"\033[1;37m          | | |\\\033[0m")
        print(" "*(63-x)+"\033[1;37m          | | >>\033[0m")
        print(" "*(63-x)+"\033[1;37m          | |\033[0m")
        print(" "*(63-x)+"\033[1;37m         /   \\\033[0m")
        print("^"*(63-x)+"\033[1;37m^^^^^^^^^^^^^^^^^^^^^^^^\033[0m")

def difficulty():



    print("Schwierigkeit wählen:")
    print("- Diese beinflusst die Anzahl der verfügbaren Züge:\n ")

    print(farbig("1. Einfach", 32) + " 15 Züge\n")
    print(farbig("2. Mittel ", 32) + " 10 Züge\n")
    print(farbig("3. Schwer ", 32) + "  5 Züge\n")
    print(farbig("4. Exit   ", 31) + " Zurück in das Menü\n")

    difficulty = 0

    while difficulty != 1 and difficulty != 2 and difficulty != 3 and difficulty != 4:

        try:
            difficulty = int(input("Zahl eingeben (1-4):\n"))
        except:
            difficulty = 0
        
        if difficulty != 1 and difficulty != 2 and difficulty != 3 and difficulty != 4:

            print("Ungültige Eingabe!")
            
    if difficulty in (1, 2, 3):
        clear_terminal()
        big_text("hangman")
        print("Schwierigkeit", difficulty, "wurde ausgewählt!\n")
        input("Enter drücken um fortzufahren:\n")
        return difficulty
    
    if difficulty == 4:
        clear_terminal()
        game_pick_mode_hangman()

def game_pick_mode_hangman():

    clear_terminal()

    big_text("hangman")

    print("Bitte Spielmodus auswählen:\n ")
    print(farbig("1. 1 v many", 32) + " mind. 1 Spieler\n---Einfach gegeneinander spielen!\n")
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
        game_hangman_1_v_many()
    
    if mode == 3:
        clear_terminal()
        return
    
def game_hangman_1_v_many():

    big_text("hangman")
    diffi = difficulty()
    clear_terminal()

    if diffi==1:

        turns_multi = 0

    elif diffi==2:

        turns_multi = 5
    else:

        turns_multi = 10

    while turns_multi <=15:
        print("Zug Nr.", turns_multi)
        print(hangman_pictures[turns_multi])
        turns_multi =  turns_multi+1

    

    print("Leider verloren)")
    input("Enter drücken um fortzufahren:\n")
    game_pick_mode_hangman()
        













if __name__ == "__main__":
    game_pick_mode_hangman()