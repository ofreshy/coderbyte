"""
Using the Python language,
have the function SudokuQuadrantChecker(strArr) read the strArr parameter being passed
which will represent a 9x9 Sudoku board of integers ranging from 1 to 9.

The rules of Sudoku are to place each of the 9 integers integer in every row and column and not have any integers repeat in the respective row, column, or 3x3 sub-grid.
The input strArr will represent a Sudoku board and it will be structured in the following format:
["(N,N,N,N,N,x,x,x,x)","(...)","(...)",...)]
where N stands for an integer between 1 and 9 and x will stand for an empty cell.

Your program will determine if the board is legal;
the board also does not necessarily have to be finished.
If the board is legal, your program should return the string legal but if it isn't legal, it should return the 3x3 quadrants (separated by commas) where the errors exist.
 The 3x3 quadrants are numbered from 1 to 9 starting from top-left going to bottom-right.

For example, if strArr is:
 ["(1,2,3,4,5,6,7,8,1)",
 "(x,x,x,x,x,x,x,x,x)",
 "(x,x,x,x,x,x,x,x,x)",
 "(1,x,x,x,x,x,x,x,x)",
 "(x,x,x,x,x,x,x,x,x)",
 "(x,x,x,x,x,x,x,x,x)",
 "(x,x,x,x,x,x,x,x,x)",
 "(x,x,x,x,x,x,x,x,x)",
 "(x,x,x,x,x,x,x,x,x)"]
 then your program should return 1,3,4 since the errors are in quadrants 1, 3 and 4 because of the repeating integer 1.

Another example, if strArr is:
["(1,2,3,4,5,6,7,8,9)"
,"(x,x,x,x,x,x,x,x,x)",
"(6,x,5,x,3,x,x,4,x)",
"(2,x,1,1,x,x,x,x,x)",
"(x,x,x,x,x,x,x,x,x)",
"(x,x,x,x,x,x,x,x,x)",
"(x,x,x,x,x,x,x,x,x)",
"(x,x,x,x,x,x,x,x,x)",
"(x,x,x,x,x,x,x,x,9)"]
then your program should return 3,4,5,9.
"""


def SudokuQuadrantChecker(strArr):
    soduko_mat = [[c for c in r.strip('()').split(",")] for r in strArr]
    quadrants = set()

    def get_quadrant(i, j):
        i_start = (i / 3) * 3
        j_start = (j / 3) * 3
        for m in range(i_start, i_start+3):
            for n in range(j_start, j_start+3):
                cell = soduko_mat[m][n]
                if cell == 'x' or (m == i and n == j):
                    continue
                yield cell

    def is_valid(i, j):
        cell = soduko_mat[i][j]

        if cell == 'x':
            return True

        if any((cell == soduko_mat[i][k] for k in range(9) if k != j)):
            return False

        if any((cell == soduko_mat[k][j] for k in range(9) if k != i)):
            return False

        if any((cell == o for o in get_quadrant(i, j))):
            return False

        return True

    for i in range(9):
        for j in range(9):
            if not is_valid(i, j):
                quadrants.add(get_quadrant_label(i, j))

    return ",".join(sorted(list(quadrants)))


def get_quadrant_label(i, j):
    return "%s" % ((j / 3) + 3 * (i / 3) + 1)
