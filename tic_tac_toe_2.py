last_update = "23.06.2025"

def big_text(text):


    if text == "tic_tac_toe_2":
        print("\033[1;31m   __  _          __                 __                 ___  \033[0m")
        print("\033[1;31m  / /_(_)____    / /_____ ______    / /_____  ___      |__ \ \033[0m")
        print("\033[1;33m / __/ / ___/   / __/ __ `/ ___/   / __/ __ \/ _ \     __/ /\033[0m")
        print("\033[1;32m/ /_/ / /__    / /_/ /_/ / /__    / /_/ /_/ /  __/    / __/ \033[0m")
        print("\033[1;34m\__/_/\___/____\__/\__,_/\___/____\__/\____/\___/____/____/ \033[0m")
        print("\033[1;34m         /_____/            /_____/            /_____/      \033[0m")
        print(" "*40+"Besser als je zuvor!")
        print(" \n \n \n \n \n")

def clear_terminal():
    # \033[H setzt den Cursor oben links, \033[J löscht bis zum Ende
    print("\033[H\033[J", end="")

def create_play_field():

    global play_field

    play_field = []
    for i in range(3):
        play_field.append([])
        for j in range(3):
            play_field[i].append(" ")  # Initialize with a space

def display_play_field():

    show_line_horizontal = "-"*13

    for i in range(len(play_field)):
        print(show_line_horizontal)
        row = "| "
        for j in range(len(play_field[i])):
            row += str(play_field[i][j]) + " | "
        print(row)
    print(show_line_horizontal)

def farbig(text, farbcode):
    return f"\033[{farbcode}m{text}\033[0m"

player = "x"

def farbig_spieler(spieler):
    if spieler == "x":
        return farbig("x", "1;31")  # rot
    elif spieler == "o":
        return farbig("o", "1;34")  # blau
    return spieler

def switch_player():
    global player
    player = "o" if player == "x" else "x"

big_text("tic_tac_toe_2")
create_play_field()
display_play_field()