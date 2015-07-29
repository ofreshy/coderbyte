
"""
given a board, decide if X or O won, is it a draw or incomplete
"""

# The hard coded 3x3 indices for a win state
wins = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],

    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],

    [(0, 0), (1, 1), (2, 2)],
    [(2, 0), (1, 1), (0, 2)],
]


def who_won(board):
    """
    :param board: a 2 dimensional matrix
    :return str: o or x if any won, draw or incomplete
    """
    incomplete = False
    for win in wins:
        seq = [board[w[0]][w[1]] for w in win]
        if all(x == 'o' for x in seq):
            return 'o'
        if all(x == 'x' for x in seq):
            return 'x'
        incomplete = incomplete or any(not x for x in seq)
    # must be a draw or incomplete
    return 'incomplete' if incomplete else 'draw'


def get_win_indices(n):
    """
    Generates the 'win' state indices for the tic-tax-toe game on an N size board

    :param n: size of board, 3 for 3x3 by board.
    :return: the indices of win states, from 0 to n-1
    """
    rows = [[(i, j) for j in xrange(n)] for i in xrange(n)]
    cols = [[(i, j) for i in xrange(n)] for j in xrange(n)]
    xs = [[(i, i) for i in xrange(n)] + [(n-i-1, i) for i in xrange(n)]]
    return rows + cols + xs


print get_win_indices(5)



def test():
    boards = [
        ([['', '', ''], ['', '', ''], ['', '', '']], 'incomplete'),
        ([['x', 'x', 'x'], ['', '', ''], ['', '', '']], 'x'),
        ([['o', '', ''], ['o', '', ''], ['o', '', '']], 'o'),
        ([['x', '', ''], ['', 'x', ''], ['', '', 'x']], 'x'),
        ([['', '', 'o'], ['', 'o', ''], ['o', '', '']], 'o'),
        ([['x', 'o', 'o'], ['o', 'x', 'x'], ['o', 'x', 'o']], 'draw'),
    ]
    for board, result in boards:
        print "expected = %s, result = %s" % (result, who_won(board))
        assert who_won(board) == result


test()










