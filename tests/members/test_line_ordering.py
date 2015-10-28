from unittest import TestCase

from members import line_ordering


class TestLineOrdering(TestCase):
    def test_example_1(self):
        input = ["A>B","A<C","C<Z"]
        actual = line_ordering.LineOrdering(input)
        self.assertEqual(actual, 1)

    def test_example_2(self):
        input = ["A>B","B<R","R<G"]
        actual = line_ordering.LineOrdering(input)
        self.assertEqual(actual, 3)

    def test_example_3(self):
        input = ["A>B"]
        actual = line_ordering.LineOrdering(input)
        self.assertEqual(actual, 1)


