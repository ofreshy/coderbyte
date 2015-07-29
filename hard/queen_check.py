"""
Using the Python language,
have the function QueenCheck(strArr) read strArr
which will be an array consisting of the locations of a Queen and King on a standard 8x8 chess board with no other pieces
on the board.
The structure of strArr will be the following:
 ["(x1,y1)","(x2,y2)"] with (x1,y1) representing the position of the queen and (x2,y2)
 representing the location of the king with x and y ranging from 1 to 8.
  Your program should determine if the king is in check based on the current positions of the pieces, and if so, return the number of spaces it can move to in order to get out of check.
  If the king is not in check, return -1.
  For example: if strArr is ["(4,4)","(6,6)"] then your program should output 6.
  Remember, because only the queen and king are on the board, if the queen is checking the king by being directly adjacent to it,
  technically the king can capture the queen.

"""


def QueenCheck(locations):
    q, k = map(eval, locations)

    def is_threat(x):
        return x != q and (x[0] == q[0] or x[1] == q[1] or abs(q[0]-x[0]) == abs(q[1]-x[1]))

    if not is_threat(k):
        return -1

    # Get all possible moves for king, including off board ones
    moves = [(k[0] + 1, k[1]), (k[0] + 1, k[1] + 1), (k[0], k[1] + 1), (k[0] - 1, k[1] + 1),
             (k[0] - 1, k[1]), (k[0] - 1, k[1] - 1), (k[0], k[1] - 1), (k[0] + 1, k[1] - 1)]

    # Filter off board moves
    r = range(1, 9)
    def is_valid_move(move):
        return move[0] in r and move[1] in r

    return len([m for m in moves if is_valid_move(m) and not is_threat(m)])



test_cases = [
    (["(4,4)", "(6,6)"], 6),
    (["(4,4)", "(8,8)"], 2),
    (["(4,4)", "(4,5)"], 3),
    (["(8,6)", "(8,8)"], 1),
    (["(1,1)", "(2,7)"], -1),

]

for test_case in test_cases:
    if QueenCheck(test_case[0]) != test_case[1]:
        print QueenCheck(test_case[0])