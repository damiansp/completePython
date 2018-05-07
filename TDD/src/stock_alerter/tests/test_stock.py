import unittest
from datetime import datetime

from ..stock import Stock, PriceRule

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



class StockTrendTest(unittest.TestCase):
    def setUp(self):
        self.goog = Stock('GOOG')

    def given_a_series_of_prices(self, prices):
        timestamps = [datetime(2014, 2, 10),
                      datetime(2014, 2, 11),
                      datetime(2014, 2, 12),
                      datetime(2014, 2, 13)]
        for timestamp, price in zip(timestamps, prices):
            self.goog.update(timestamp, price)

    def test_increasing_trend_is_true_if_price_increases_for_3_updates(self):
        self.given_a_series_of_prices([8, 10, 12])
        self.assertTrue(self.goog.is_increasing_trend())

    def test_increasing_trend_is_false_if_price_decreases(self):
        self.given_a_series_of_prices([8, 12, 10])
        self.assertFalse(self.goog.is_increasing_trend())

    def test_increasing_trend_is_false_if_price_equal(self):
        self.given_a_series_of_prices([8, 10, 10])
        self.assertFalse(self.goog.is_increasing_trend())
        


class PriceRuleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        goog = Stock('GOOG')
        goog.update(datetime(2014, 2, 10), 11)
        cls.exchange = {'GOOG': goog}

    def test_a_PriceRule_matches_when_it_meets_the_condition(self):
        rule = PriceRule('GOOG', lambda stock: stock.price > 10)
        self.assertTrue(rule.matches(self.exchange))

    def test_a_PriceRule_is_False_if_the_condition_is_not_met(self):
        rule = PriceRule('GOOG', lambda stock: stock.price < 10)
        self.assertFalse(rule.matches(self.exchange))

    def test_a_PriceRule_is_False_it_the_stock_is_not_int_the_exchange(self):
        rule = PriceRule('MSFT', lambda stock: stock.price > 10)
        self.assertFalse(rule.matches(self.exchange))

    def test_a_PriceRule_is_False_if_the_stock_hasnt_gotten_an_update_yet(self):
        self.exchange['AAPL'] = Stock('AAPL')
        rule = PriceRule('AAPL', lambda stock: stock.price > 10)
        self.assertFalse(rule.matches(self.exchange))

    def test_a_PriceRule_only_depends_on_its_stock(self):
        rule = PriceRule('MSFT', lambda stock: stock.price > 10)
        self.assertEqual({'MSFT'}, rule.depends_on())
