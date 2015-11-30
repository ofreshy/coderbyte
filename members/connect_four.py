"""
Using the Python language,
have the function ConnectFourWinner(strArr) read the strArr parameter being passed
which will represent a 6x7 Connect Four board.
The rules of the game are:
two players alternate turns and place a colored disc down into the grid from the top and the disc falls down the column
until it hits the bottom or until it hits a piece beneath it.
The object of the game is to connect four of one's own discs of the same color next to each other
vertically, horizontally, or diagonally before your opponent.
The input strArr will represent a Connect Four board and it will be structured in the following format:
["R/Y","(R,Y,x,x,x,x,x)","(...)","(...)",...)]
where R represents the player using red discs,
Y represents the player using yellow discs
and x represents an empty space on the board.
The first element of strArr will be either R or Y and it represents whose turn it is.
Your program should determine,
based on whose turn it is,
whether a space exists that can give that player a win.
If a space does exist your program should return the space in the following format:
(RxC) where R=row and C=column.
If no space exists, return the string none.
The board will always be in a legal setup.

For example, if strArr is: ["R","(x,x,x,x,x,x,x)","(x,x,x,x,x,x,x)","(x,x,x,x,x,x,x)","(x,x,x,R,x,x,x)","(x,x,x,R,x,x,x)","(x,x,x,R,Y,Y,Y)"] then your program should return (3x4).

Another example, if strArr is: ["Y","(x,x,x,x,x,x,x)","(x,x,x,x,x,x,x)","(x,x,x,x,x,x,x)","(x,x,Y,Y,x,x,x)","(x,R,R,Y,Y,x,R)","(x,Y,R,R,R,Y,R)"] then your program should return (3x3).

"""

from itertools import chain


class Board(object):
    @classmethod
    def from_str_arr(cls, strArr):
        matrix = [row.strip('()').split(',') for row in strArr[1:]]
        return cls(matrix)

    def __init__(self, matrix):
        self.mat = matrix
        self.N = len(matrix)
        self.M = len(matrix[0])

    def get(self, i, j):
        return self.mat[i][j]

    def get_cells_below_me(self, i, j):
        return [self.mat[x][j] for x in range(i+1, self.N)]

    def get_horizontal_neighbours(self, i, j):
        sj = max(0, j-3)
        ej = min(self.M, j+4) - 3
        for k in range(sj, ej):
            yield [self.mat[i][x] for x in range(k, k+4)]

    def get_vertical_neighbours(self, i, j):
        si = max(0, i-3)
        ei = min(self.N, i+4) - 3
        for k in range(si, ei):
            yield [self.mat[x][j] for x in range(k, k+4)]

    def get_diagonal_neighbours(self, i, j):
        for k in range(-3, 1):
            ilow, ihigh = i-k, i-k-3
            jleft, jright = j+k, j+k+3
            if ilow < self.N and ihigh >= 0 and jleft >= 0 and jright < self.M:
                yield [self.mat[i-x][j+x] for x in range(k, k+4)]

        for k in range(-3, 1):
            ilow, ihigh = i-k, i-k-3
            jright, jleft = j-k, j-k-3
            if ilow < self.N and ihigh >= 0 and jleft >= 0 and jright < self.M:
                yield [self.mat[i-x][j-x] for x in range(k, k+4)]

    def get_neighbours(self, i, j):
        return chain(
            self.get_horizontal_neighbours(i, j),
            self.get_vertical_neighbours(i, j),
            self.get_diagonal_neighbours(i, j),
        )

    def iter_indices(self):
        for i in range(self.N-1, -1, -1):
            for j in range(self.M-1, -1, -1):
                yield i, j


def ConnectFourWinner(strArr):
    color, board = strArr[0], Board.from_str_arr(strArr)

    def cannot_slot(i, j):
        for cell in board.get_cells_below_me(i, j):
            if cell == 'x':
                return True
        return False

    def is_winning_slot(i, j):
        if board.get(i, j) != 'x':
            return False
        if cannot_slot(i, j):
            return False

        for neighbour in board.get_neighbours(i, j):
            if neighbour.count(color) == 3:
                return True
        return False

    for ii, jj in board.iter_indices():
        if ii == 2 and jj == 3:
            pass
        if is_winning_slot(ii, jj):
            return "(%sx%s)" % (ii+1, jj+1)
    return "none"
