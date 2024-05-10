import unittest

# noinspection PyProtectedMember
from hello_ext._hello_impl import hello
from numpy import pi


class TestHi(unittest.TestCase):

    def test_hi(self):
        self.assertAlmostEqual(3.14159265358979, pi)
        self.assertEqual("Whassup, sucka?", hello())
