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

words_offline = [
    "Haus", "Baum", "Auto", "Straße", "Fahrrad",
    "Wasser", "Feuer", "Luft", "Erde", "Himmel",
    "Hund", "Katze", "Vogel", "Fisch", "Pferd",
    "laufen", "springen", "schlafen", "denken", "sehen",
    "reden", "schreiben", "lesen", "lernen", "spielen",
    "schön", "groß", "klein", "schnell", "langsam",
    "hell", "dunkel", "kalt", "warm", "freundlich",
    "rot", "blau", "grün", "gelb", "weiß",
    "Buch", "Tisch", "Stuhl", "Fenster", "Tür",
    "Liebe", "Angst", "Freude", "Hoffnung", "Mut"
]

letter_ls =[]
wrong_letters_ls = [] 

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

def word_input():

    clear_terminal()

    big_text("hangman")

    print("Jetzt das geheimsnissvolle Wort eingeben:\n")
    word = str(input())
    global letter_ls
    letter_ls = [] 

    for letter in word:
        letter_ls.append(letter)

def guess_word():
    global letter_ls
    global wrong_letters_ls

    diffi = difficulty()
    word_input()
    show = ["_" for _ in letter_ls]

    # Setze die erlaubte Anzahl an Fehlversuchen je nach Schwierigkeitsgrad
    if diffi == 1:
        max_turns = 15
    elif diffi == 2:
        max_turns = 10
    else:
        max_turns = 5

    turns = 0
    wrong_letters_ls = []

    while turns < max_turns and "_" in show:
        clear_terminal()
        big_text("hangman")
        print(f"Zug Nr. {turns + 1} von {max_turns}")

        # Bild proportional zur Fehleranzahl anzeigen
        pic_index = min(int(turns * (len(hangman_pictures) - 1) / max_turns), len(hangman_pictures) - 1)
        print(hangman_pictures[pic_index] + "\n")

        print("Wort: " + " ".join(show))
        print("Falsche Buchstaben: " + ", ".join(wrong_letters_ls))
        print("Buchstaben-Tipp abgeben:\n")
        guess = input().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Bitte genau einen Buchstaben eingeben!")
            input("Enter drücken...")
            continue

        if guess.upper() in wrong_letters_ls or guess in [l.lower() for l in show]:
            print("Buchstabe wurde schon geraten!")
            input("Enter drücken...")
            continue

        found = False
        for index, letter in enumerate(letter_ls):
            if letter.lower() == guess:
                show[index] = letter
                found = True

        if found:
            print("Treffer!\n")
        else:
            print("Das war wohl nix!")
            wrong_letters_ls.append(guess.upper())
            turns += 1

        input("Enter drücken für den nächsten Zug...")

    clear_terminal()
    big_text("hangman")
    # Nach Spielende das finale Bild anzeigen
    pic_index = min(int(turns * (len(hangman_pictures) - 1) / max_turns), len(hangman_pictures) - 1)
    print(hangman_pictures[pic_index])
    if "_" not in show:
        print("Glückwunsch! Das Wort war:", "".join(letter_ls))
    else:
        print("Leider verloren! Das Wort war:", "".join(letter_ls))

    letter_ls = []
    wrong_letters_ls = []
    input("Enter drücken um fortzufahren:\n")

def game_pick_mode_hangman():

    clear_terminal()

    big_text("hangman")

    print("Bitte Spielmodus auswählen:\n ")
    print(farbig("1. 1 v many", 32) + " mind. 2 Spieler\n---Einer gibt ein, die anderen raten!\n")
    print(farbig("2. Computer  ", 32) + " 1 Spieler\n---Gegen den Computer Spielen                  (noch nicht verfügbar)\n")
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

    clear_terminal()
    big_text("hangman")
    guess_word()
    game_pick_mode_hangman()
        
if __name__ == "__main__":
    game_pick_mode_hangman()