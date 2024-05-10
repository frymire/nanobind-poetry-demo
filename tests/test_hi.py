import unittest

from numpy import pi

from hello import hello


class TestHi(unittest.TestCase):

    def test_hi(self):
        self.assertAlmostEqual(3.14159265358979, pi)
        self.assertEqual("Whassup, sucka?", hello.say_hi_cpp())
