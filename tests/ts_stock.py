import unittest
from stockBuilder import StockBuilder


class TestStock(unittest.TestCase):
    def testTakeTopReturnsExpected(self):
        self.assertEqual(len(StockBuilder().build().takeTop(10)), 10)

    def testTakeTopReturnsEmptyWhenEmpty(self):
        self.assertEqual(len(StockBuilder()
                             .setNumberOfCards(0).build()
                             .takeTop(10)), 0)
