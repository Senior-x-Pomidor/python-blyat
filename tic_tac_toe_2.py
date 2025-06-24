import tic_tac_toe
def clear_terminal():
    # \033[H setzt den Cursor oben links, \033[J löscht bis zum Ende
    print("\033[H\033[J", end="")

def farbig(text, farbcode):
    return f"\033[{farbcode}m{text}\033[0m"

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

##############################################################################################################################################################################################
player ="o"

def create_field():

    global field 

    field = []

    for row in range(3):
        field.append([])
        for collumn in range(3):
            field[row].append(" ")

def display_field():

    line_out_len = 13 

    for row in range(len(field)):
        print("-" * line_out_len)  # line out
        for collumn in range(len(field[row])):
            print("| ", end="")  # collumn line out
            print(field[row][collumn], end=" ")  # content out
        print("|")  # End the row with a closing pipe and newline
    print("-" * line_out_len)  # Print the bottom line after the last row

def create_state():

    global state_dict

    state_dict ={(row, collumn):" " for row in range(len(field)) for collumn in range(len(field[row]))}

def switch_player():
    global player
    player = "o" if player == "x" else "x"

def update_field_from_state():

    global field

    for row in range(len(field)):
        for collumn in range(len(field[row])):
            field[row][collumn] = state_dict[(row, collumn)]

def update_state_from_field():

    global state_dict

    for row in range(len(field)):
        for collumn in range(len(field[row])):
            state_dict[(row, collumn)] = field[row][collumn]

def move_on_field():

    row = 0
    collumn = 0
    choice = "DasIstFantastisch"
    colored_player = farbig(player, "1;32") #Player_cursor ist grün
    while choice == "DasIstFantastisch":
        clear_terminal()
        big_text("tic_tac_toe_2")
        update_field_from_state()
        field[row][collumn] = colored_player
        display_field()
        

        move = input("(w,a,s,d dann Enter) zum Bewegen, (Enter für Auswahl)\n").lower()

        if move == "w" and row > 0:                           #Kollisionsbedingung
            row = row-1 

        if move == "s" and row < len(field) - 1:
            row = row+1
        if move == "a" and collumn > 0:
            collumn = collumn-1
        if move == "d" and collumn < len(field[0]) - 1:
            collumn = collumn+1
        if move == "" and state_dict[(row, collumn)] == " ":
            if player == "o": #gesetzes element ändert farbe
                colored_player = farbig(player, "1;34")
                field[row][collumn] = colored_player
            else:
                colored_player = farbig(player, "1;31")
                field[row][collumn] = colored_player
            break
        
    update_state_from_field()
    
def check_win():
    
    #check in rows

    for row in range(len(field)):

        if state_dict[(row, 0)] == state_dict[(row, 1)] == state_dict[(row, 2)] and state_dict[row, 0] != " ":

            return True
        
    for collumn in range (len(field[0])):

        if state_dict[(0, collumn)] == state_dict[(1, collumn)] == state_dict[(2, collumn)] and state_dict[(0, collumn)] != " ":

            return True

    # Check diagonals
    if state_dict[(0, 0)] == state_dict[(1, 1)] == state_dict[(2, 2)] and state_dict[(0, 0)] != " ":
        return True
    if state_dict[(0, 2)] == state_dict[(1, 1)] == state_dict[(2, 0)] and state_dict[(0, 2)] != " ":
        return True

    return False



def main_tic_tac_toe_2():

    create_field()
    create_state()

    while True:
        big_text("tic_tac_toe_2")
        switch_player()
        move_on_field()

        if check_win() == True:
            clear_terminal()
            big_text("tic_tac_toe_2")
            display_field()
            print("Spieler " + player + " hat gewonnen!")
            input("Enter drücken...")
            break
        elif " " not in state_dict.values():
            clear_terminal()
            big_text("tic_tac_toe_2")
            display_field()
            print("Unentschieden!")
            input("Enter drücken...")
            break
    clear_terminal()
    tic_tac_toe.game_pick_mode_tic_tac_toe()




if __name__ == "__main__":
    main_tic_tac_toe_2()