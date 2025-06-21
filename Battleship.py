wasser = f"\033[1;34m~\033[0m"


field_show = [
    [[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser]],
    [[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser]],
    [[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser]],
    [[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser]],
    [[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser]],
    [[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser]],
    [[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser]],
    [[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser]],
    [[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser]],
    [[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser],[wasser]] 
]

field_place = [
    [[], [], [], [], [], [], [], [], [], []],  
    [[], [], [], [], [], [], [], [], [], []],  
    [[], [], [], [], [], [], [], [], [], []],  
    [[], [], [], [], [], [], [], [], [], []], 
    [[], [], [], [], [], [], [], [], [], []],  
    [[], [], [], [], [], [], [], [], [], []],  
    [[], [], [], [], [], [], [], [], [], []],  
    [[], [], [], [], [], [], [], [], [], []], 
    [[], [], [], [], [], [], [], [], [], []], 
    [[], [], [], [], [], [], [], [], [], []]    
]

letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
ships_to_place = [[4], [3], [2], [1]]
ships_location =[]

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
    j_coord = input("Bitte Buchstaben eingeben:")
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

        t = f"\033[1;31m{"T"}\033[0m"
        
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


    direction = input("Ausrichtung eingeben (H für Horizontal, V für Vertikal):")

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
    while not all(elem[0] == 0 for elem in ships_to_place):
        field_place_out()
        place_ship()
    field_place_out()
            
def lets_sink_ships():
    i = 1
    for y in range(75):
        print(".")
    while True:
        print(f"Runde Nr.", i)

        field_show_out()
        check_for_hit()
        check_for_destruction()
        if all(ship['destroyed'] for ship in ships_location):
            print("Alle Schiffe sind versenkt! Spiel beendet.")
            field_show_out()
            break
        i = i+1




placement_part()
lets_sink_ships()