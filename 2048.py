import random

field_size = 4
board = [[' ' for _ in range(field_size)] for _ in range(field_size)]

def print_board():
    for row in board:
        for field in row:
            print(f'[{field}]', end='')
        print()


print_board()

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
    board[picked_field[0]][picked_field[1]] = new_tile

print()
add_random_tile()
print_board()