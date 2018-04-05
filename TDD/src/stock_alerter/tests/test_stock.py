import unittest
from datetime import datetime

from ..stock import Stock

# Common asserts:
# assertAlmostEqual assertNotAlmostEqual
# assertEqual       assertNotEqual
# assertGreater     assertGreaterEqual
# assertIn          assertNotIn
# assertIs          assertIsNot
# assertIsInstance  assertNotIsInstance
# assertIsNone      assertIsNotNone
# assertLess        assertLessEqual
# assertRegex       assertNotRegex
# assertTrue        assertFalse 
# assertRaises
# fail

class StockTest(unittest.TestCase):
    # override default setUp. this code run before every test.
    def setUp(self):
        self.goog = Stock('GOOG')
        
    def test_price_of_a_new_stock_class_should_be_None(self):
        self.assertIsNone(self.goog.price)

    def test_stock_update(self):
        '''An update should set the price on the stock object. 
        The timestamp uses the datetime module.'''
        self.goog.update(datetime(2014, 2, 12), price=10)
        self.assertEqual(10, self.goog.price)

    def test_negative_price_should_throw_ValueError(self):
        #with self.assertRaises(ValueError):
        #    self.goog.update(datetime(2014, 2, 13), -1) # SAME AS:
        self.assertRaises(
            ValueError, self.goog.update, datetime(2014, 2, 13), -1)

    def test_stock_price_should_give_the_latest_price(self):
        self.goog.update(datetime(2014, 2, 12), price=10)
        self.goog.update(datetime(2014, 2, 13), price=8.4)
        self.assertAlmostEqual(self.goog.price, 8.4, delta=0.0001)
        #self.assertAlmostEqual(self.goog.price, 8.4, places=4) # alt option

    def test_increasing_trend_is_true_if_price_increases_for_3_updates(self):
        timestamps = [datetime(2014, 2, i) for i in range(11, 14)]
        prices = [8, 10, 12]
        for timestamp, price in zip(timestamps, prices):
            self.goog.update(timestamp, price)
        self.assertTrue(self.goog.is_increasing_trend())
