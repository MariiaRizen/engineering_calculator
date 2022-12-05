import unittest
import math


def sinus(number):
    return math.sin(number)


def cosinus(number):
    return math.cos(number)


def factorial(number):
    return math.factorial(number)


def radical(number):
    return math.sqrt(number)


def power(x, y):
    if x < 0 and 0 < y < 1:
        raise ValueError
    return math.pow(x, y)


def tangens(number):
    return math.tan(number)


def add(x, y):
    return x + y


def minus(x, y):
    return x - y


def div(x, y):
    return x / y


def multiplication(x, y):
    return x * y


class Test(unittest.TestCase):
    def test_sin(self):
        self.assertEqual(sinus(math.radians(0)), 0)

    def test_cos(self):
        self.assertEqual(cosinus(math.pi), -1)

    def test_factorial(self):
        self.assertEqual(factorial(3), 6)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-4)

    def test_radical(self):
        self.assertEqual(radical(4), 2)

    def test_power(self):
        self.assertEqual(power(3, 3), 27)

    def test_power_negative(self):
        with self.assertRaises(ValueError):
            power(-3, 0.4)

    def test_tangens(self):
        self.assertEqual(tangens(math.radians(0)), 0)

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_minus(self):
        self.assertEqual(minus(4, 5), -1)

    def test_div(self):
        self.assertEqual(div(6, 3), 2)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(-3, 0)

    def test_multiplication(self):
        self.assertEqual(multiplication(4, 5), 20)


if __name__ == '__main__':
    unittest.main()
