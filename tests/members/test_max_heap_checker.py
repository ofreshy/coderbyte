from unittest import TestCase

from members import max_heap


class TestMaxHeapChecker(TestCase):
    def test_1(self):
        self.assertEqual("max", max_heap.MaxHeapChecker([100, 19, 36, 17]))

    def test_2(self):
        self.assertEqual("19,52", max_heap.MaxHeapChecker([10, 19, 52, 13, 16]))

    def test_3(self):
        self.assertEqual("19,52", max_heap.MaxHeapChecker([10, 19, 52, 13, 16]))

    def test_4(self):
        self.assertEqual("5,10", max_heap.MaxHeapChecker([1, 5, 10, 2, 3, 10, 1]))
