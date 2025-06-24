last_update = "24.06.2025"

import tic_tac_toe_2

def clear_terminal():
    # \033[H setzt den Cursor oben links, \033[J löscht bis zum Ende
    print("\033[H\033[J", end="")

def farbig(text, farbcode):
    return f"\033[{farbcode}m{text}\033[0m"

def big_text(text):

        if text == "tic_tac_toe":

            print("\033[1;31m  ______ _            ______                  ______           \033[0m")
            print("\033[1;31m /_  __/(_)_____     /_  __/____ _ _____     /_  __/____   ___ \033[0m")
            print("\033[1;33m  / /  / // ___/      / /  / __ `// ___/      / /  / __ \ / _ \\""\033[0m")
            print("\033[1;32m / /  / // /__       / /  / /_/ // /__       / /  / /_/ //  __/\033[0m")
            print("\033[1;34m/_/  /_/ \___/______/_/   \__,_/ \___/______/_/   \____/ \___/ \033[0m")
            print("\033[1;34m             /_____/                 /_____/                   \033[0m")
            print("by dani (Senior-x-Pomidor) "+last_update)
            print(" \n \n \n \n \n")


field = [[" "," "," "],[" "," "," "],[" "," "," "]]
empty = " "



def game_tic_tac_toe_1v1():

    for line in field:
        line.clear()                    
        line.extend([" "] * 3)  


    win = False

    for i in range(9):

        if win:
            break

        #print(i)
        if i%2 == 0:
            player = "x"
        else:
            player = "o"

        while True:
            line = 0
            column = 0
            try:
                line    =    int(input("line     :"))-1
                column  =    int(input("column   :"))-1
            except:
                print("Please enter a number!")
                continue

            if line <= 2 and column <=2:

                if field[line][column] == empty  or field[line][column] == empty:
                    field[line].pop(column)
                    field[line].insert(column, player)

                    for line in field:
                        print("")

                        for column in line:
                            print(f"[{column}]",end="" )

                    break

                else:
                    print("Field is already occupied!\nTry again!")

            else:
                print("Input is to hight!\nTry again! ")

        for line in field:

            if line.count(player) == 3:
                win = True
                print("\n\nPlayer",player,"won!")
                input("Drücke Enter zum beenden:")
                for row in field:
                    line.clear()
                    line.extend([" "] * 3)
                break

        for column in range(3):

            if win:
                break

            a = "a"

            for line in range(3):

                if a != field[line][column] and line > 0 or field[line][column] == " ":
                    break

                if line == 2:
                    win = True
                    print("\n\nPlayer", player, "won!")
                    input("Drücke Enter zum beenden:")
                    for line in field:
                        line.clear()
                        line.extend([" "] * 3)  
                    break

                a = field[line][column]

        if ((field[0][0] == field[1][1] == field[2][2]) or (field[0][2] == field[1][1] == field[2][0])) and field[1][1] != " ":
            win = True
            print("\n\nPlayer", player, "won!")
            input("Drücke Enter zum beenden:")
            for line in field:
                line.clear()
                line.extend([" "] * 3)  
            break

        if i < 8 and not win:
            print("\n\nNext turn!")
        elif not win:
            print("\n\nIt is a draw!")
            input("Drücke Enter zum beenden:")
            for line in field:
                line.clear()                    
                line.extend([" "] * 3)  
            break
    clear_terminal()
    game_pick_mode_tic_tac_toe()



def game_pick_mode_tic_tac_toe():

    big_text("tic_tac_toe")

    print("Bitte Spielmodus auswählen:\n ")
    print(farbig("1. 1v1            ", 32) + " 2 Spieler\n---Einfach gegeneinander spielen!\n")
    print(farbig("2. Computer       ", 32) + " 1 Spieler\n---Gegen den Computer Spielen            (noch nicht verfügbar)\n")
    print(farbig("3. tic_tac_toe_2  ", 32) + " Neuer, Schöner, Besser! \n")
    print(farbig("4. Exit           ", 31) + " \n---Spiel schließen\n")



    mode = 0

    while mode != 1 and mode != 2 and mode != 3 and mode != 4:

        try:
            mode = int(input("Zahl eingeben (1-4):"))
        except:
            mode = 0
        
        if mode != 1 and mode != 2 and mode != 3 and mode != 4:

            print("Ungültige Eingabe!")
            
    if mode == 1:
        clear_terminal()
        game_tic_tac_toe_1v1()

    
    if mode == 3:
        clear_terminal()
        tic_tac_toe_2.main_tic_tac_toe_2()


    if mode == 4:
        clear_terminal()
        return

if __name__ == "__main__":
    game_pick_mode_tic_tac_toe()