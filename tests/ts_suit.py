import unittest
from suit import Suit
from color import Color


class TestSuit(unittest.TestCase):
    def setUp(self):
        self.suitSut = Suit.HEARTS
        self.suitSut.color = Color.BLACK

    def testFindHearts(self):
        self.assertEqual(Suit.find('H'), Suit.HEARTS)

    def testFindNonPossible(self):
        self.assertIsNone(Suit.find('Ñ'))

    def testInitials(self):
        self.assertEqual(Suit.initials(), ['h', 'd', 'c', 'p'])

    def testGetColor(self):
        self.assertEqual(Color.BLACK, self.suitSut.getColor())
