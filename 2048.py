import random

board_size = 4
board = [[' ' for _ in range(board_size)] for _ in range(board_size)]

def print_board():
    for row in board:
        for field in row:
            print(f'[{field}]', end='')
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

    elif direction == 'A':
        print('move left')
        for i, row in enumerate(board):
            for j, field in enumerate(row):
                x = j
                while x > 0 and row[x - 1] == ' ':
                    x -= 1
                board[i][j] = ' '
                board[i][x] = field

    elif direction == 'S':
        print('move down')

    elif direction == 'D':
        print('move right')
        for i, row in enumerate(board):
            for j, field in reversed(list(enumerate(row))):
                x = j
                while x < len(row) - 1 and row[x + 1] == ' ':
                    x += 1
                board[i][j] = ' '
                board[i][x] = field

    else:
        print('input error')
        return
    
    add_random_tile()
    print_board()


def start_game():
    add_random_tile()
    print_board()

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


start_game()