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

def check_winner():
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if play_field[i][0] == play_field[i][1] == play_field[i][2] != " ":
            return play_field[i][0]
        if play_field[0][i] == play_field[1][i] == play_field[2][i] != " ":
            return play_field[0][i]
    if play_field[0][0] == play_field[1][1] == play_field[2][2] != " ":
        return play_field[0][0]
    if play_field[0][2] == play_field[1][1] == play_field[2][0] != " ":
        return play_field[0][2]
    return None

def is_full():
    for row in play_field:
        if " " in row:
            return False
    return True

def place_on_field():
    global play_field, player

    if not hasattr(place_on_field, "x"):
        place_on_field.x = 0
    if not hasattr(place_on_field, "y"):
        place_on_field.y = 0

    x = place_on_field.x
    y = place_on_field.y

    while True:
        temp_field = [row[:] for row in play_field]
        if temp_field[y][x] == " ":
            temp_field[y][x] = player
        clear_terminal()  # Terminal nach jedem Zug leeren
        big_text("tic_tac_toe_2")
        print(f"Spieler {farbig_spieler(player)} ist am Zug.")
        display_play_field_with_cursor(temp_field)
        move = input("(w/a/s/d für bewegen, Enter zum Setzen): ").lower()

        if move == "":
            if play_field[y][x] == " ":
                play_field[y][x] = player
                place_on_field.x = x
                place_on_field.y = y
                break
            else:
                print("Feld ist bereits belegt!")
                continue
        elif move == "s":
            orig_y = y
            for _ in range(len(play_field)):
                y = (y + 1) % len(play_field)
                if play_field[y][x] == " ":
                    break
            else:
                y = orig_y  # keine freie Zelle gefunden
        elif move == "w":
            orig_y = y
            for _ in range(len(play_field)):
                y = (y - 1) % len(play_field)
                if play_field[y][x] == " ":
                    break
            else:
                y = orig_y
        elif move == "d":
            orig_x = x
            for _ in range(len(play_field[0])):
                x = (x + 1) % len(play_field[0])
                if play_field[y][x] == " ":
                    break
            else:
                x = orig_x
        elif move == "a":
            orig_x = x
            for _ in range(len(play_field[0])):
                x = (x - 1) % len(play_field[0])
                if play_field[y][x] == " ":
                    break
            else:
                x = orig_x

def display_play_field_with_cursor(field):
    show_line_horizontal = "-"*13
    for i in range(len(field)):
        print(show_line_horizontal)
        row = "| "
        for j in range(len(field[i])):
            cell = field[i][j]
            if cell == "x" or cell == "o":
                row += farbig_spieler(cell) + " | "
            else:
                row += str(cell) + " | "
        print(row)
    print(show_line_horizontal)

def display_play_field():
    show_line_horizontal = "-"*13

    for i in range(len(play_field)):
        print(show_line_horizontal)
        row = "| "
        for j in range(len(play_field[i])):
            cell = play_field[i][j]
            if cell == "x" or cell == "o":
                row += farbig_spieler(cell) + " | "
            else:
                row += str(cell) + " | "
        print(row)
    print(show_line_horizontal)

create_play_field()

def play_tic_tac_toe_2():

    winner = None
    while not is_full() and not winner:
        clear_terminal()  # Terminal vor jedem Zug leeren
        big_text("tic_tac_toe_2")
        print(f"Spieler {farbig_spieler(player)} ist am Zug.")
        display_play_field()
        place_on_field()
        winner = check_winner()
        if not winner:
            switch_player()

    clear_terminal()
    big_text("tic_tac_toe_2")
    display_play_field()
    if winner:
        print("Es war eine fesselde Schlacht!")
        print(f"Spieler {farbig_spieler(winner)} hat gewonnen!")
        input("Enter drücken...")
    else:
        print("Unentschieden!")
        input("Enter drücken...")


if __name__ == "__main__":
    play_tic_tac_toe_2()