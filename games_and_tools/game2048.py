import random
import math

board_size = 4
field_size = 4
board = [[' ' for _ in range(board_size)] for _ in range(board_size)]

def calc_digits(field):
    try:
        number = int(field)
        return math.floor(math.log(number, 10)) + 1
        # note: log(1000, 10) equals 2.99999 here
    except:
        return 1


def calc_score():
    score = 0
    for row in board:
        for field in row:
            if field != ' ':
                score += int(field)

    return score


def clear_terminal():
    print("\033[H\033[J", end="")


def print_board():
    print('_' * (field_size + 2) * board_size)
    for row in board:
        for field in row:
            digits = calc_digits(field)
            print(f"[{' ' * (field_size - digits)}{field}]", end='')
        print()
    print('‾' * (field_size + 2) * board_size)


def print_turn():
    clear_terminal()

    print("""_______________      _____   ______  
\_____  \   _  \    /  |  | /  __  \ 
 /  ____/  /_\  \  /   |  |_>      < 
/       \  \_/   \/    ^   /   --   \\
\_______ \_____  /\____   |\______  /
        \/     \/      |__|       \/
""")
    print('            by Boris - 24.06.2025')
    print()
    print()
    print('current score: ', calc_score())
    
    
    print_board()

    print()
    print()
    print('w, a, s, d and enter to move')
    print('q to quit')
    print()
    print()

def add_random_tile():
    new_tile = 2
    free_fields = []

    # determine free fields
    for i, row in enumerate(board):
        for j, field in enumerate(row):
            if field == ' ':
                free_fields.append((i, j))

    # pick a free field
    picked_field = random.choice(free_fields)

    # set the picked field to new tile
    board[picked_field[0]][picked_field[1]] = new_tile


def play_move(direction):

    if direction == 'W':
        print('move up')
        for i, row in enumerate(board):
            for j, field in enumerate(row):
                x = i
                while x > 0 and board[x - 1][j] == ' ':
                    x -= 1

                if x > 0 and board[x - 1][j] == field:
                    x -= 1
                    field += field

                board[i][j] = ' '
                board[x][j] = field

    elif direction == 'A':
        print('move left')
        for i, row in enumerate(board):
            for j, field in enumerate(row):
                x = j
                while x > 0 and row[x - 1] == ' ':
                    x -= 1
                
                if x > 0 and row[x - 1] == field:
                    x -= 1
                    field += field

                board[i][j] = ' '
                board[i][x] = field

    elif direction == 'S':
        print('move down')
        for i, row in reversed(list(enumerate(board))):
            for j, field in enumerate(row):
                x = i
                while x < len(board) - 1 and board[x + 1][j] == ' ':
                    x += 1

                if x < len(board) - 1 and board[x + 1][j] == field:
                    x += 1
                    field += field

                board[i][j] = ' '
                board[x][j] = field


    elif direction == 'D':
        print('move right')
        for i, row in enumerate(board):
            for j, field in reversed(list(enumerate(row))):
                x = j
                while x < len(row) - 1 and row[x + 1] == ' ':
                    x += 1

                if x < len(row) - 1 and row[x + 1] == field:
                    x += 1
                    field += field

                board[i][j] = ' '
                board[i][x] = field

    else:
        print('input error')
        return
    
    add_random_tile()
    print_turn()


def start():
    add_random_tile()
    print_turn()

    while True:
        i = input()
        i = i.capitalize()
        if i == 'Q' or i == 'EXIT':
            break

        if i != 'W' and i != 'A' and i != 'S' and i != 'D':
            print('Ungültige Eingabe!')
            continue

        play_move(i)

    print('game over')


if __name__ == '__main__':
    start()