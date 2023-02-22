puzzle =   [[5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]]


# print puzzle more tidy to see
def show_puzzle(puzzle):
    print(' '*5, end='')
    print(*range(9), sep='  ')
    print('-'*32)
    for index, row in enumerate(puzzle):
        print(index, '|', end=' ')
        print(row)
    print('\n')

# check there isn't any empty col
def is_full(puzzle):
    return all(all(row) for row in puzzle)

# check the puzzle is completely valid
correct_set = set(range(1, 10))
def is_correct(puzzle):
    return all(not correct_set.symmetric_difference(row) for row in puzzle)

def deep_copy(puzzle):
    return [row.copy() for row in puzzle]

# get possible numbers for specified position
def get_possible_numbers(puzzle, row_index, col_index):
    numbers = set(range(1, 10))
    numbers.difference_update(puzzle[row_index])
    numbers.difference_update([row[col_index] for row in puzzle])
    return tuple(numbers)


# get info list about empty columns. First element is row_index, second is col_index, third is possible numbers
# function sorted based on possible numbers count for performance purposes
def get_sorted_empty_cols_info(puzzle):
    cols_info = []
    for row_index, row in enumerate(puzzle):
        for col_index, col in enumerate(row):
            if col == 0:
                cols_info.append((row_index, col_index, get_possible_numbers(puzzle, row_index, col_index)))
    cols_info.sort(key=lambda col_info: len(col_info[2]))
    return cols_info



def sudoku(puzzle):
    # if completely filled and puzzle is valid then return puzzle, except return False
    if is_full(puzzle):
        return is_correct(puzzle) and puzzle
    cols_info = get_sorted_empty_cols_info(puzzle)
    # if there are col_info that has empty possible numbers that means it's invalid and must return False
    if any(not info[2] for info in cols_info):
        return False
    # will fill empty field orderly from less count of possible numbers to more count of possible numbers
    min_col_info = cols_info[0]
    
    # copy puzzle to avoid changing inner elements while cheking
    new_puzzle = deep_copy(puzzle)
    
    # you can remove comment to see visually how function fill the puzzle
    # import time, os
    # show_puzzle(puzzle)
    # time.sleep(0.2)
    # os.system('cls' if os.name == 'nt' else 'clear')
    row_index, col_index, possible_numbers = min_col_info
    for number in possible_numbers:
        new_puzzle[row_index][col_index] = number
        result = sudoku(new_puzzle)
        # if result is not False or is puzzle array that means everything is ok and must return that completed puzzle
        if result:
            return result
            


show_puzzle(sudoku(puzzle))
print(is_correct(sudoku(puzzle)))

