from unittest import TestCase

from members import soduko_checkers


class TestSodukoChecker(TestCase):
    def test_example_1(self):
        soduko_board = [
            "(1,2,3,4,5,6,7,8,9)",
            "(x,x,x,x,x,x,x,x,x)",
            "(6,x,5,x,3,x,x,4,x)",
            "(2,x,1,1,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,9)",
        ]
        self.assertEqual(soduko_checkers.SudokuQuadrantChecker(soduko_board), "3,4,5,9")

    def test_example_2(self):
        soduko_board = [
            "(1,2,3,4,5,6,7,8,1)",
            "(x,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)",
            "(1,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)"
        ]
        self.assertEqual(soduko_checkers.SudokuQuadrantChecker(soduko_board), "1,3,4")

    def test_example_3(self):
        soduko_board = (
            "(1,2,3,4,5,6,7,8,9)",
            "(x,x,x,x,x,x,x,x,x)",
            "(6,x,5,x,3,x,x,4,x)",
            "(2,x,1,5,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,8)",
        )

        self.assertEqual(soduko_checkers.SudokuQuadrantChecker(soduko_board), "legal")


    def test_empty_board(self):
        soduko_board = [
            "(x,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)",
            "(1,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)",
            "(x,x,x,x,x,x,x,x,x)"
        ]
        self.assertEqual(soduko_checkers.SudokuQuadrantChecker(soduko_board), "legal")


