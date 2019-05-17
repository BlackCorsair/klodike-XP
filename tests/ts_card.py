import unittest
from card import Card
from suit import Suit
from color import Color
from number import Number


class TestCard(unittest.TestCase):
    def setUp(self):
        self.suitDOC = Suit.CLOVERS
        self.suitDOC.color = Color.BLACK
        self.cardSUT = Card(self.suitDOC, Number.TWO)

    def testFlipChangesFacedUp(self):
        previous = self.cardSUT.isFacedUp()
        self.assertNotEqual(previous, self.cardSUT.flip().isFacedUp())

    def testIsNextToCardTruePlus1(self):
        self.assertTrue(self.cardSUT.isNextToCard(
            Card(self.suitDOC, Number.THREE)))

    def testIsNextToCardTrueLess1(self):
        self.assertTrue(self.cardSUT.isNextToCard(
            Card(self.suitDOC, Number.ACE)))

    def testIsNextToCardTrueEquals(self):
        self.assertTrue(self.cardSUT.isNextToCard(
            Card(self.suitDOC, Number.TWO)))

    def testIsNextToCardFalse(self):
        self.assertFalse(self.cardSUT.isNextToCard(
            Card(self.suitDOC, Number.FOUR)))

    def testIsNextToCardNonPossible(self):
        self.assertIsNone(self.cardSUT.isNextToCard(1))

    def testIsFacedUpFalse(self):
        self.assertFalse(self.cardSUT.isFacedUp())
