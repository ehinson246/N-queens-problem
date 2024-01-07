#!/usr/bin/env python3

N = 4

EMPTY_SQUARE = 0

ATTACKED_SQUARE = 1

QUEEN_SQUARE = 2

ATTACKED_QUEEN = ATTACKED_SQUARE + QUEEN_SQUARE

# board_position = None

def generate_empty_board_rows():
    empty_rows = []
    empty_row = []
    while len(empty_rows) < N:
        while len(empty_row) < N:
            empty_row.append(EMPTY_SQUARE)
        new_row = empty_row.copy()
        empty_rows.append(new_row)
    return empty_rows

# from here on out, c is the actual column - 1
def update_horizontal_vision(board_position, row, column):
    for c in range(N):
        square = board_position[row - 1][c]
        if square & ATTACKED_SQUARE:
            pass
        else:
            board_position[row - 1][c] += ATTACKED_SQUARE
    board_position[row - 1][column - 1] = QUEEN_SQUARE

# from here on out, r is the actual row - 1
def update_vertical_vision(board_position, row, column):
    for r in range(N):
        square = board_position[r][column - 1]
        if square & ATTACKED_SQUARE:
            pass
        else:
            board_position[r][column - 1] += ATTACKED_SQUARE
    board_position[row - 1][column - 1] = QUEEN_SQUARE

def update_top_left_diagonal(board_position, row, column, squares_until_top, squares_until_left):
    r = row - 1
    c = column - 1
    if squares_until_top == 0 or squares_until_left == 0:
        pass
    elif squares_until_top >= squares_until_left:
        for i in range(1, column):
            square = board_position[r - i][c - i]
            if square & ATTACKED_SQUARE:
                pass
            else:
                board_position[r - i][c - i] += ATTACKED_SQUARE
    elif squares_until_top < squares_until_left:
        for i in range(1, row):
            square = board_position[r - i][c - i]
            if square & ATTACKED_SQUARE:
                pass
            else:
                board_position[r - i][c - i] += ATTACKED_SQUARE

def update_top_right_diagonal(board_position, row, column, squares_until_top, squares_until_right):
    r = row - 1
    c = column - 1
    if squares_until_top == 0 or squares_until_right == 0:
        pass
    elif squares_until_top >= squares_until_right:
        for i in range(1, (squares_until_right + 1)):
            square = board_position[r - i][c + i]
            if square & ATTACKED_SQUARE:
                pass
            else:
                board_position[r - i][c + i] += ATTACKED_SQUARE
    elif squares_until_top < squares_until_right:
        for i in range(1, row):
            square = board_position[r - i][c + i]
            if square & ATTACKED_SQUARE:
                pass
            else:
                board_position[r - i][c + i] += ATTACKED_SQUARE

def update_bottom_left_diagonal(board_position, row, column, squares_until_bottom, squares_until_left):
    r = row - 1
    c = column - 1
    if squares_until_bottom == 0 or squares_until_left == 0:
        pass
    elif squares_until_bottom >= squares_until_left:
        for i in range(1, column):
            square = board_position[r + i][c - i]
            if square & ATTACKED_SQUARE:
                pass
            else:
                board_position[r + i][c - i] += ATTACKED_SQUARE
    elif squares_until_bottom < squares_until_left:
        for i in range(1, (squares_until_bottom + 1)):
            square = board_position[r + i][c - i]
            if square & ATTACKED_SQUARE:
                pass
            else:
                board_position[r + i][c - i] += ATTACKED_SQUARE

def update_bottom_right_diagonal(board_position, row, column, squares_until_bottom, squares_until_right):
    r = row - 1
    c = column - 1
    if squares_until_bottom == 0 or squares_until_right == 0:
        pass
    elif squares_until_bottom >= squares_until_right:
        for i in range(1, (squares_until_right + 1)):
            square = board_position[r + i][c + i]
            if square & ATTACKED_SQUARE:
                pass
            else:
                board_position[r + i][c + i] += ATTACKED_SQUARE
    elif squares_until_bottom < squares_until_right:
        for i in range(1, (squares_until_bottom + 1)):
            square = board_position[r + i][c + i]
            if square & ATTACKED_SQUARE:
                pass
            else:
                board_position[r + i][c + i] += ATTACKED_SQUARE

def update_diagonal_vision(board_position, row, column):
    squares_until_top = row - 1
    squares_until_bottom = N - row
    squares_until_left = column - 1
    squares_until_right = N - column
    update_top_left_diagonal(board_position, row, column, squares_until_top, squares_until_left)
    update_top_right_diagonal(board_position, row, column, squares_until_top, squares_until_right)
    update_bottom_left_diagonal(board_position, row, column, squares_until_bottom, squares_until_left)
    update_bottom_right_diagonal(board_position, row, column, squares_until_bottom, squares_until_right)

def update_queen_vision(board_position, row, column):
    update_horizontal_vision(board_position, row, column)
    update_vertical_vision(board_position, row, column)
    update_diagonal_vision(board_position, row, column)

def add_queen_to_board(board_position, row, column):
    board_position[row - 1][column - 1] = QUEEN_SQUARE
    update_queen_vision(board_position, row, column)

def check_for_attacked_queens(board_position):
    any_attacked_queens = False
    for row in board_position:
        attacked_queen_count = row.count(ATTACKED_QUEEN)
        if attacked_queen_count > 0:
            any_attacked_queens = True
            break
    return any_attacked_queens

def construct_trial_board(valid_squares_so_far):
    trial_board_position = generate_empty_board_rows()
    row = 0
    for column in valid_squares_so_far:
        row += 1
        add_queen_to_board(trial_board_position, row, column)
    return trial_board_position

def find_solution():
    # the index for valid squares corresponds with the row - 1, and the value is the column
    valid_squares_so_far = []
    # failed_trial_columns = []
    # next_backtrack_trial_column = None
    current_row = 1
    trial_column = 1

    while current_row <= N:

        trial_board_position = construct_trial_board(valid_squares_so_far)
        # for row in trial_board_position:
        #     print(row)

        trial_square = trial_board_position[current_row - 1][trial_column - 1]
        # print(trial_square)

        while trial_square > 0:
            trial_column += 1
            if trial_column > N:
                trial_column = valid_squares_so_far[-1]
                valid_squares_so_far.pop(-1)
                current_row -= 1
                if current_row == 0:
                    return None
            trial_square = trial_board_position[current_row - 1][trial_column - 1]   
        # print(trial_column)

        add_queen_to_board(trial_board_position, current_row, trial_column)
        # for row in trial_board_position:
        #     print(row)
        any_attacked_queens = check_for_attacked_queens(trial_board_position)

        if any_attacked_queens:
            # print("Attacked queen!")
            trial_column += 1
            if trial_column > N:
                trial_column = valid_squares_so_far[-1]
                valid_squares_so_far.pop(-1)
                current_row -= 1
                if current_row == 0:
                    return None
        else:
            # print("No attacked queens.")
            valid_squares_so_far.append(trial_column)
            trial_column = 1
            current_row += 1
    
    solution = construct_trial_board(valid_squares_so_far)
    return solution

def print_solution():
    solution = find_solution()
    if solution is None:
        print(f"\nNo solution for a {N}x{N} board.\n")
    else:
        for row in solution:
            print(row)

print_solution()