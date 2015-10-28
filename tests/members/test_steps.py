from unittest import TestCase

from members import steps


class TestSteps(TestCase):
    def test_1(self):
        self.assertEqual(1, steps.StepWalking(1))

    def test_2(self):
        self.assertEqual(2, steps.StepWalking(2))

    def test_numbers(self):
        expected = {
            3: 3,
            4: 5,
            5: 8,
        }
        actual = {k: steps.StepWalking(k) for k in expected.keys()}
        self.assertDictEqual(expected, actual)


