import unittest
from card import Card
from suit import Suit
from color import Color
from number import Number


class CardBuilder():
    def __init__(self):
        self.suit = Suit.CLOVERS
        self.suit.color = Color.BLACK
        self.number = Number.TWO
        self.facedUp = False

    def setColor(self, color):
        self.suit.color = color
        return self

    def setSuit(self, suit):
        self.suit = suit
        return self

    def setNumber(self, number):
        self.number = number
        return self

    def setFaceUp(self):
        self.facedUp = True
        return self

    def build(self):
        if self.facedUp:
            builded = Card(self.suit, self.number)
            builded.facedUp = self.facedUp
            return builded
        return Card(self.suit, self.number)


class TestCard(unittest.TestCase):
    def setUp(self):
        self.cardSUT = CardBuilder().build()

    def tearDown(self):
        self.cardSUT = None

    def testFlipChangesFacedUp(self):
        previous = self.cardSUT.isFacedUp()
        self.assertNotEqual(previous, self.cardSUT.flip().isFacedUp())

    def testIsNextToCardTruePlus1(self):
        self.assertTrue(self.cardSUT.isNextToCard(
            CardBuilder().setNumber(Number.THREE).build()))

    def testIsNextToCardTrueLess1(self):
        self.assertTrue(self.cardSUT.isNextToCard(
            CardBuilder().setNumber(Number.ACE).build()))

    def testIsNextToCardTrueEquals(self):
        self.assertTrue(self.cardSUT.isNextToCard(
            CardBuilder().setNumber(Number.TWO).build()))

    def testIsNextToCardFalse(self):
        self.assertFalse(self.cardSUT.isNextToCard(
            CardBuilder().setNumber(Number.FOUR).build()))

    def testIsNextToCardNonPossible(self):
        self.assertIsNone(self.cardSUT.isNextToCard(1))

    def testIsFacedUpFalse(self):
        self.assertFalse(self.cardSUT.isFacedUp())
