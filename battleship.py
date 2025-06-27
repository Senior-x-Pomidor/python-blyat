last_update = "27.06.2025"

def clear_terminal():
    # \033[H setzt den Cursor oben links, \033[J löscht bis zum Ende
    print("\033[H\033[J", end="")

wasser = f"\033[1;34m~\033[0m"

field_show =  []

field_place = []

ships_to_place = []

ships_location = []


def reset_field(contents):


    new_field = []
    for z in range(10):
        new_field.append([])
        for zz in range(10):
            new_field[z].append(list(contents))
    return new_field

def reset_fields():

    global field_show
    global field_place

    field_show  = reset_field([wasser]) 
    field_place = reset_field([])

def reset_game():

    reset_fields()

    global ships_to_place 
    global ships_location
    ships_to_place = [[4], [3], [2], [1]]
    ships_location = []




letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]



def farbig(text, farbcode):
    return f"\033[{farbcode}m{text}\033[0m"

def field_show_out():
    print(" ")
    print(" ")
    print(" "*4, end ="")
    print("   ".join(letter_list))
    for i in range(10):
        print(" "*1,"-"*41)
        print(i,"|", end="")
        for j in range(10):
            cell = field_show[i][j]
            content = str(cell[0]) if cell else " "
            print(f" {content} |", end="")
        print()
    print(" "*1,"-"*41)

def field_place_out():
    print(" ")
    print(" ")
    print(" "*4, end ="")
    print("   ".join(letter_list))
    for i in range(10):
        print(" "*1,"-"*41)
        print(i,"|", end="")
        for j in range(10):
            cell = field_place[i][j]
            content = str(cell[0]) if cell else " "
            print(f" {content} |", end="")
        print()
    print(" "*1,"-"*41)

def j_cord_pick():
    j_coord = input("Bitte Buchstaben eingeben:").upper()
    if j_coord in letter_list:
        letter_list.index
        return letter_list.index(j_coord)
        
    else:
        print("Ungültige Eingabe. Bitte einen Buchstaben von A bis J eingeben.")
        return j_cord_pick()
        
def i_cord_pick():
    try:
        i_coord = int(input("Bitte Zahl eingeben (0-9): "))
        if 0 <= i_coord <= 9:
            return i_coord
        else:
            print("Ungültige Eingabe. Bitte eine Zahl von 0 bis 9 eingeben.")
            return i_cord_pick()
    except ValueError:
        print("Ungültige Eingabe. Bitte eine Zahl von 0 bis 9 eingeben.")
        return i_cord_pick()

def check_for_destruction():
    """
    Prüft für jedes Schiff in ships_location, ob alle Segmente getroffen sind.
    Setzt 'destroyed'=True und ersetzt 'T' durch 'X' bei vollständiger Zerstörung.
    """
    for ship in ships_location:
        # Überspringe bereits zerstörte Schiffe
        if ship['destroyed']:
            continue

        # Prüfe, ob alle Koordinaten getroffen wurden
        t = f"\033[1;31mx\033[0m"
        all_hit = all(
            field_show[i][j][0] == t
            for (i, j) in ship['coords']
        )

        # Wenn vollständig getroffen, markiere als zerstört und ersetze Marker
        
        if all_hit:
            ship['destroyed'] = True
            print(f"Schiff der Länge {ship['length']} wurde zerstört!")
            for (i, j) in ship['coords']:
                x = f"\033[1;32mX\033[0m"
                field_show[i][j] = [x]

def check_for_hit():


    j = j_cord_pick()
    i = i_cord_pick()
    if field_place[i][j]:
        print("Treffer!")
        t = f"\033[1;31mx\033[0m"
        field_show[i][j] = [t]
    else:
        print("Daneben!")
        o = f"\033[1;36mo\033[0m"
        field_show[i][j] = [o]

def place_ship():

    while True:
        print("Noch verfügbare Schiffe:")
        for q in range(len(ships_to_place)):
            print(f"L{q+1}", ":", ships_to_place[q][0])
        try:
            l = int(input("Länge (1, 2, 3, 4): "))
        except ValueError:
            print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
            continue
        if not (1 <= l <= len(ships_to_place)):
            print("Ungültige Schiffsgröße, bitte zwischen 1 und 4 wählen.")
            continue
        if ships_to_place[l-1][0] <= 0:
            print(f"Keine Schiffe der Länge {l} mehr verfügbar. Bitte anderes wählen.")
            continue
        break

    # 2. Koordinaten abfragen
    j = j_cord_pick()
    i = i_cord_pick()




    #Richung Hori oder Vert


    direction = input("Ausrichtung eingeben (H für Horizontal, V für Vertikal):").upper()

    if direction == "H":
        coords = [(i, j + n) for n in range(l)]
    elif direction == "V":
        coords = [(i + n, j) for n in range(l)]
    else:
        print("Ungültige Richtung.")
        return place_ship()

    # Check if all coordinates are valid
    for (ii, jj) in coords:
        if not (0 <= ii < 10 and 0 <= jj < 10):
            print("Schiff passt nicht ins Spielfeld!")
            return place_ship()
    
    if any(field_place[ii][jj] for ii, jj in coords):
            print("Eine oder mehrere Zellen sind bereits belegt. Bitte neu wählen.")
            return place_ship()
    
    ships_to_place[l-1][0] -= 1
    ships_location.append({
        'length': l,
        'coords': coords,
        'destroyed': False
    })

    for (ii, jj) in coords:
        field_place[ii][jj].append(l)

def placement_part():
    reset_game()
    while not all(elem[0] == 0 for elem in ships_to_place):
        big_text("legacy")
        field_place_out()
        place_ship()
        clear_terminal()
    field_place_out()
      
def lets_sink_ships():

    i = 1
    while True:

        big_text("legacy")
        print(f"Runde Nr.", i)
        field_show_out()
        check_for_hit()
        check_for_destruction()
        clear_terminal()
        if all(ship['destroyed'] for ship in ships_location):
            big_text("legacy")
            field_show_out()
            print("Alle Schiffe sind versenkt! Spiel beendet.")
            input("Drücke Enter zum beenden:")
            break
        i = i+1








#Game start and modes

def big_text(text):


    if text == "schiffe_versenken":

        print("\033[1;31m   _____      __    _ ________       _    __                          __            \033[0m")
        print("\033[1;31m  / ___/_____/ /_  (_) __/ __/__    | |  / /__  _____________  ____  / /_____  ____ \033[0m")
        print("\033[1;33m  \__ \/ ___/ __ \/ / /_/ /_/ _ \   | | / / _ \/ ___/ ___/ _ \/ __ \/ //_/ _ \/ __ \\""\033[0m")
        print("\033[1;32m ___/ / /__/ / / / / __/ __/  __/   | |/ /  __/ /  (__  )  __/ / / / ,< /  __/ / / /\033[0m")
        print("\033[1;34m/____/\___/_/ /_/_/_/ /_/  \___/____|___/\___/_/  /____/\___/_/ /_/_/|_|\___/_/ /_/ \033[0m")
        print("\033[1;34m                              /_____/                                               \033[0m")
        print("by dani (Senior-x-Pomidor) "+last_update)
        print("  \n \n \n \n \n")

    elif text == "legacy":
        print("\033[1;31m      __                                    \033[0m")
        print("\033[1;31m     / /   ___   ____ _ ____ _ _____ __  __ \033[0m")
        print("\033[1;31m    / /   / _ \ / __ `// __ `// ___// / / / \033[0m")
        print("\033[1;31m   / /___/  __// /_/ // /_/ // /__ / /_/ /  \033[0m")
        print("\033[1;31m  /_____/\___/ \__, / \__,_/ \___/ \__, /   \033[0m")
        print("\033[1;31m              /____/              /____/    \033[0m")

def legacy():
    placement_part()
    clear_terminal()
    lets_sink_ships()
    clear_terminal()
    game_pick_mode_battleship()

def game_pick_mode_battleship():

    big_text("schiffe_versenken")

    print("Bitte Spielmodus auswählen:\n ")
    print(farbig("1. Legacy  ", 32) + " 2 Spieler, 2 Geräte\n---Spieler plazieren zunächst Schiffe beim Gegener, danach beginnt das Spiel!\n")
    print(farbig("2. Normal  ", 32) + " 2 Spieler, 1 Gerät \n---Spieler plazieren abwächselnd Schiffe, danach beginnt das Spiel!                (noch nicht verfügbar)\n")
    print(farbig("3. Computer", 32) + " 1 Spieler, 1 Gerät \n---Spieler plaziert Schiffe, danach beginnt das Spiel!                             (noch nicht verfügbar)\n")
    print(farbig("4. Exit    ", 31) + " \n---Spiel schließen\n")

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
        legacy()
    


    if mode == 4:
        clear_terminal()
        return



if __name__ == "__main__":
    game_pick_mode_battleship()






