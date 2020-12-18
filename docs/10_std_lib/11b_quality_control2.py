import unittest

def mean(vals):
    return sum(vals) / len(vals)


class TestStats(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([20, 30, 70]),  40.)
        self.assertEqual(round(mean([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            mean([])
        with self.assertRaises(TypeError):
            mean(1, 2, 3)


print(unittest.main())
