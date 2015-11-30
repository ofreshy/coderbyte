from unittest import TestCase

from members import simple_sat


class TestSimpleSat(TestCase):
    def test_example_1(self):
        self.assertEqual(simple_sat.SimpleSAT("((a&c)&~a)"), "no")

    def test_example_2(self):
        self.assertEqual(simple_sat.SimpleSAT("(a&b)|c"), "yes")

    def test_simple_yes(self):
        self.assertEqual(simple_sat.SimpleSAT("a"), "yes")

    def test_simple_no(self):
        self.assertEqual(simple_sat.SimpleSAT("a & ~a"), "no")

    def test_5_letters(self):
        self.assertEquals(simple_sat.SimpleSAT("a&(b|c)&~b&~c"), "no")


