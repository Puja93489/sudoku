def find_next_empty(puzzle):
    
    for r in range(9):
        for c in range(9): 
            if puzzle[r][c]== -1:
                return r,c
    return None, None 
def is_valid(puzzle, guess, row, col):
    
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
        
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row //3) * 3 
    col_start = (col // 3)* 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False


    
    return True

def solve_sudoku(puzzle):
    
    row, col = find_next_empty(puzzle)

   
    if row is None:
        return True
    
    for guess in range(1, 10): 
       
        if is_valid(puzzle, guess, row, col):
            
            puzzle[row][col] =  guess
            if solve_sudoku(puzzle):
                return True
            
        
        puzzle[row][col] = -1 

    return False


def get_user_input():
    print("Enter Sudoku row by row (use 0 or -1 for empty cells)")
    board = []

    for i in range(9):
        while True:
            row = input(f"Row {i+1}: ").split()

            if len(row) != 9:
                print("❌ Enter exactly 9 numbers!")
                continue

            try:
                row = [int(x) if int(x) != 0 else -1 for x in row]
                board.append(row)
                break
            except:
                print("❌ Only numbers allowed!")

    return board


def print_board(board):
    print("\nSolved Sudoku:\n")
    for row in board:
        print(" ".join(str(num) for num in row))


if __name__ == '__main__':
    puzzle = get_user_input()

    if solve_sudoku(puzzle):
        print_board(puzzle)
    else:
        print("❌ No solution exists!")
    
      