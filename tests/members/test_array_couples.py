from unittest import TestCase

from members import array_couples


class TestSteps(TestCase):
    def test_1(self):
        self.assertEqual("yes", array_couples.ArrayCouples([4, 5, 1, 4, 5, 4, 4, 1]))

    def test_2(self):
        self.assertEqual("5,14,14,1", array_couples.ArrayCouples([6, 2, 2, 6, 5, 14, 14, 1]))

    def test_0(self):
        self.assertEqual("yes", array_couples.ArrayCouples([]))
