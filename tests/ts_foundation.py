import unittest
from klondike.number import Number
from klondike.foundation import Foundation
from suitBuilder import SuitBuilder
from cardBuilder import CardBuilder


class TestFoundation(unittest.TestCase):
    def setUp(self):
        self.foundationSUT = Foundation(SuitBuilder().build())

    def tearDown(self):
        self.foundationSUT = None

    def testIsCompleteTrue(self):
        self.foundationSUT.push(CardBuilder().setNumber(Number.KING).build())
        self.assertTrue(self.foundationSUT.isComplete())

    def testIsCompleteFalse(self):
        self.assertFalse(self.foundationSUT.isComplete())

    def testFitsInFalseDifferentSuit(self):
        self.assertFalse(self.foundationSUT.fitsIn(
            CardBuilder().setSuit(SuitBuilder().
                                  setInitial('h').build()).build()))

    def testFitsInFalseButIsComplete(self):
        self.foundationSUT.push(CardBuilder().setNumber(Number.KING).build())
        self.assertFalse(self.foundationSUT.fitsIn(CardBuilder()
                                                   .setSuit(SuitBuilder()
                                                            .build()).build()))

    def testFitsInTrueStockEmptyAndCardIsSameSuit(self):
        self.assertTrue(self.foundationSUT.fitsIn(CardBuilder().build()))

    def testGetSuit(self):
        self.assertEqual(self.foundationSUT.getSuit(), SuitBuilder().build())
