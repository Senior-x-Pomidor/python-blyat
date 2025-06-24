field_size = 4
board = [[' ' for _ in range(field_size)] for _ in range(field_size)]

def print_board():
    for row in board:
        for field in row:
            print(f'[{field}]', end='')
        print()


print_board()