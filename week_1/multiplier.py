import unittest


def factorize(x):
    """ Factorize integer positive and return its factors.
        :type x: int,>=0
        :rtype: int,N>0
    """
    if x == 0:
        return 1
    else:
        return x * factorize(x - 1)


class TestFactorization(unittest.TestCase):
    def test_simple_multipliers(self):
        x = 77
        a, b = factorize(x)
        self.assertEqual(a*b, x)


if __name__ == "__main__":
    unittest.main()
