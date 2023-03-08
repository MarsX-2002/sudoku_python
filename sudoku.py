def is_valid(puzzle, row, col, num):
    """
    Check if placing a number at a given position is valid
    """
    # Check row
    if num in puzzle[row]:
        return False
    
    # Check column
    if num in [puzzle[i][col] for i in range(9)]:
        return False
    
    # Check subgrid
    subgrid_row = (row // 3) * 3
    subgrid_col = (col // 3) * 3
    subgrid = [puzzle[subgrid_row+i][subgrid_col+j] for i in range(3) for j in range(3)]
    if num in subgrid:
        return False
    
    return True


def solve_sudoku(puzzle, row=0, col=0):
    """
    Solve a 9x9 Sudoku puzzle using a recursive backtracking algorithm
    """
    if row == 9:  # Base case: we have filled in all rows
        return puzzle
    
    next_row = row if col < 8 else row + 1
    next_col = (col + 1) % 9
    
    if puzzle[row][col] != 0:  # Skip cells that already have a number
        return solve_sudoku(puzzle, next_row, next_col)
    
    for num in range(1, 10):
        if is_valid(puzzle, row, col, num):
            puzzle[row][col] = num  # Place the number in the puzzle
            if solve_sudoku(puzzle, next_row, next_col):  # Recurse to next cell
                return puzzle
            puzzle[row][col] = 0  # Backtrack if no valid solution was found
    
    return False  # No valid solution found


# Example usage
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solution = solve_sudoku(puzzle)
if solution:
    for row in solution:
        print(row)
else:
    print("No solution found")
