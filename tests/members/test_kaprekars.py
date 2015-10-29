from unittest import TestCase

from members import kaprekars


class TestSteps(TestCase):
    def test_example_1(self):
        self.assertEqual(kaprekars.KaprekarsConstant(2111), 5)

    def test_example_2(self):
        self.assertEqual(kaprekars.KaprekarsConstant(9381), 7)

    def test_6174(self):
        self.assertEqual(kaprekars.KaprekarsConstant(6174), 0)


