last_update = "23.06.2025"

def clear_terminal():
    # \033[H setzt den Cursor oben links, \033[J löscht bis zum Ende
    print("\033[H\033[J", end="")

def create_play_field():

    global play_field

    play_field = []
    for i in range(3):
        play_field.append([])
        for j in range(3):
            play_field[i].append([])

def display_play_field():
    global play_field

    content = "x"

    show_line_horizontal = "-"*13

    show_lines_vertical_and_content = (("| "+ content +" ")*3 +"|")

    for _ in range (len(play_field)):

        print(show_line_horizontal)
        print(show_lines_vertical_and_content)
    print(show_line_horizontal)
    
create_play_field()
display_play_field()