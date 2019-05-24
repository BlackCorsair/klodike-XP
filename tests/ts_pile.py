import unittest
import pytest
from pileBuilder import PileBuilder
from cardBuilder import CardBuilder
from suitBuilder import SuitBuilder
from klondike.number import Number


class TestPile(unittest.TestCase):
    def setUp(self):
        self.pileSUT = PileBuilder().build()

    def tearDown(self):
        self.pileSUT = None

    def testFitsInFalseDifferentSuit(self):
        self.assertFalse(self.pileSUT.fitsIn(
            CardBuilder().setSuit(SuitBuilder().
                                  setInitial('h').build()).build()))

    def testFitsInFalseButIsComplete(self):
        self.pileSUT.push(CardBuilder().setNumber(Number.KING).build())
        self.assertFalse(self.pileSUT.fitsIn(CardBuilder()
                                             .setSuit(SuitBuilder()
                                                      .build()).build()))

    def testFitsInTrueStockEmptyAndCardIsSameSuit(self):
        self.assertTrue(self.pileSUT.fitsIn(CardBuilder().build()))

    def testGetTopReturnsMaxCardsWhenAskForMoreCardsThanInPile(self):
        self.assertEqual(len(self.pileSUT.getTop(5)), 3)

    def testGetTopReturnsEmptyWhenPileIsEmpty(self):
        self.assertEqual(PileBuilder()
                         .setNumber(0).setFacedUpCards(0)
                         .build().getTop(1), [])

    def testGetTopReturnsEmptyListWhenAskingZero(self):
        self.assertEqual(self.pileSUT.getTop(0), [])

    def testGetTopReturnsSameAmount(self):
        self.assertEqual(len(self.pileSUT.getTop(1)), 1)

    def testAddToTopCardFacedDownRaiseError(self):
        with pytest.raises(Exception):
            self.pileSUT.addToTop(CardBuilder().build())

    def testAddToTopWhenTopFacedDownRaiseError(self):
        with pytest.raises(Exception):
            self.pileSUT.addToTop(CardBuilder().setFaceUp().build())

    def testRemoveTopActuallyRemoves(self):
        self.pileSUT.removeTop(3)
        self.assertTrue(self.pileSUT.empty())

    def testNumberOfFacedUpCardsReturnsOne(self):
        self.assertEqual(self.pileSUT.getNumberOfFacedUpCards(), 1)

    def testNumberOfFacedUpCardsReturnsZero(self):
        self.assertEqual(PileBuilder()
                         .setFacedUpCards(0).build()
                         .getNumberOfFacedUpCards(), 0)

    def testGetCardsReturnFullStack(self):
        self.assertEqual(len(self.pileSUT.getCards()), 3)

    def testGetCardsReturnEmptyListWhenEmpty(self):
        self.assertEqual(PileBuilder()
                         .setNumber(0).setFacedUpCards(0).build()
                         .getCards(), [])
