from unittest import TestCase

from members import connect_four

MAT_1 = [
 #  ['0', '1', '2', '3', '4', '5']
    ['x', 'x', 'x', 'x', 'x', 'x'],  #0
    ['x', 'x', 'x', 'x', 'Y', 'x'],  #1
    ['x', 'x', 'x', 'x', 'R', 'x'],  #2
    ['x', 'x', 'x', 'x', 'Y', 'x'],  #3
    ['x', 'x', 'x', 'x', 'R', 'x'],  #4
    ['x', 'R', 'x', 'x', 'Y', 'x'],  #5
    ['R', 'Y', 'x', 'x', 'R', 'x'],  #6
]


class TestBoard(TestCase):
    def test_below_me_when_bottom(self):
        board = connect_four.Board(MAT_1)
        self.assertEqual(board.get_cells_below_me(6, 0), [])

    def test_below_me_when_middle(self):
        board = connect_four.Board(MAT_1)
        self.assertEqual(board.get_cells_below_me(4, 0), ['x', 'R'])

    def test_below_me_when_top(self):
        board = connect_four.Board(MAT_1)
        self.assertEqual(board.get_cells_below_me(0, 0), ['x', 'x', 'x', 'x', 'x', 'R'])

    def test_horizontal_neighbours_left_corner(self):
        board = connect_four.Board(MAT_1)
        neighbours = list(board.get_horizontal_neighbours(6, 0))
        self.assertEqual(len(neighbours), 1)
        self.assertEqual(neighbours, [['R', 'Y', 'x', 'x']])

    def test_horizontal_neighbours_left_2_slides(self):
        board = connect_four.Board(MAT_1)
        neighbours = list(board.get_horizontal_neighbours(6, 1))
        self.assertEqual(len(neighbours), 2)
        self.assertEqual(neighbours, [['R', 'Y', 'x', 'x'], ['Y', 'x', 'x', 'R']])

    def test_horizontal_neighbours_right_corner(self):
        board = connect_four.Board(MAT_1)
        neighbours = list(board.get_horizontal_neighbours(6, 5))
        self.assertEqual(neighbours, [['x', 'x', 'R', 'x']])

    def test_horizontal_neighbours_middle(self):
        board = connect_four.Board(MAT_1)
        neighbours = list(board.get_horizontal_neighbours(6, 2))
        self.assertEqual(neighbours,
        [
            ['R', 'Y', 'x', 'x'],
            ['Y', 'x', 'x', 'R'],
            ['x', 'x', 'R', 'x'],
        ])

    def test_vertical_neighbours_bottom(self):
        board = connect_four.Board(MAT_1)
        neighbours = list(board.get_vertical_neighbours(6, 4))
        self.assertEqual(
            neighbours,
            [['Y', 'R', 'Y', 'R']]
        )

    def test_vertical_neighbours_top(self):
        board = connect_four.Board(MAT_1)
        neighbours = list(board.get_vertical_neighbours(0, 0))
        self.assertEqual(
            neighbours,
            [['x', 'x', 'x', 'x']]
        )

    def test_vertical_neighbours_middle(self):
        board = connect_four.Board(MAT_1)
        neighbours = list(board.get_vertical_neighbours(3, 0))
        self.assertEqual(
            neighbours,
            [
                ['x', 'x', 'x', 'x'],
                ['x', 'x', 'x', 'x'],
                ['x', 'x', 'x', 'x'],
                ['x', 'x', 'x', 'R'],
            ]
        )

    def test_diagonal_neighbours_bottom_left(self):
        board = connect_four.Board(MAT_1)
        neighbours = list(board.get_diagonal_neighbours(6, 0))
        self.assertEqual(
            neighbours,
            [['R', 'R', 'x', 'x']]
        )

    def test_diagonal_neighbours_mid_left(self):
        board = connect_four.Board(MAT_1)
        neighbours = list(board.get_diagonal_neighbours(4, 2))
        self.assertEqual(
            neighbours,
            [
                ['R', 'R', 'x', 'x'],
                ['R', 'x', 'x', 'R'],
                ['x', 'x', 'R', 'x'],
                ['R', 'x', 'x', 'x'],
                ['x', 'x', 'x', 'x'],
            ]
        )

    def test_diagonal_neighbours_mid_left2(self):
        board = connect_four.Board(MAT_1)
        neighbours = list(board.get_diagonal_neighbours(5, 1))
        self.assertEqual(
            neighbours,
            [
                ['R', 'R', 'x', 'x'],
                ['R', 'x', 'x', 'R'],
            ]
        )

    def test_diagonal_neighbours_top_left(self):
        board = connect_four.Board(MAT_1)
        neighbours = list(board.get_diagonal_neighbours(0, 5))
        self.assertEqual(
            neighbours,
            [
                ['x', 'x', 'Y', 'x'],
            ]
        )

    def test_diagonal_neighbours_bottom_left(self):
        board = connect_four.Board(MAT_1)
        neighbours = list(board.get_diagonal_neighbours(6, 5))
        self.assertEqual(
            neighbours,
            [
                ['x', 'Y', 'x', 'x'],
            ]
        )


class TestConnectFourWinners(TestCase):
    def test_case_1(self):
        strArr = ["R","(x,x,x,x,x,x,x)","(x,x,x,x,x,x,x)","(x,x,x,x,x,x,x)","(x,x,x,R,x,x,x)","(x,x,x,R,x,x,x)","(x,x,x,R,Y,Y,Y)"]
        ans = connect_four.ConnectFourWinner(strArr)
        self.assertEqual(ans, '(3x4)')

    def test_case_2(self):
        strArr = ["Y","(x,x,x,x,x,x,x)","(x,x,x,x,x,x,x)","(x,x,x,x,x,x,x)","(x,x,Y,Y,x,x,x)","(x,R,R,Y,Y,x,R)","(x,Y,R,R,R,Y,R)"]
        ans = connect_four.ConnectFourWinner(strArr)
        self.assertEqual(ans, '(3x3)')
