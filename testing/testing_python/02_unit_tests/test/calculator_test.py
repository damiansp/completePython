import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))

    def test_add_method_raises_typeError_if_not_ints(self):
        self.assertRaises(TypeError, self.calc.add, 'hello', 'world')


if __name__ == '__main__':
    unittest.main()
