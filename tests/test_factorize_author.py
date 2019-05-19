import unittest


def factorize(x):
    """ Factorize integer positive and return its factors.
        :type x: int,>=0
        :rtype: tuple[N],N>0
    """
    pass


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        for x in 1.5, 'string':
            with self.subTest(x=x):
                with self.assertRaises(TypeError):
                    factorize(x)

    def test_negative(self):
        for x in -1, -10, -100:
            with self.subTest(x=x):
                with self.assertRaises(ValueError):
                    factorize(x)

    def test_zero_and_one_cases(self):
        for x in 0, 1:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), (x,))

    def test_simple_numbers(self):
        for x in 3, 13, 29:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), (x,))

    def test_two_simple_multipliers(self):
        with self.subTest(x=6):
            self.assertEqual(factorize(6), (2, 3))
        with self.subTest(x=26):
            self.assertEqual(factorize(26), (2, 13))
        with self.subTest(x=121):
            self.assertEqual(factorize(121), (11, 11))

    def test_many_multipliers(self):
        with self.subTest(x=1001):
            self.assertEqual(factorize(1001), (7, 11, 13))
        with self.subTest(x=9699690):
            self.assertEqual(factorize(9699690), (2, 3, 5, 7, 11, 13, 17, 19))


if __name__ == "__main__":
    unittest.main()
