import unittest
from number import Number
from cardBuilder import CardBuilder


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
