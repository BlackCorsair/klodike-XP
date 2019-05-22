import unittest
from foundation import Foundation
from suitBuilder import SuitBuilder
from cardBuilder import CardBuilder


class TestFoundation(unittest.TestCase):
    def setUp(self):
        self.foundationSUT = Foundation(SuitBuilder().build())

    def testIsCompleteTrue(self):
        self.assertTrue(self.foundationSUT.isComplete())

    @unittest.expectedFailure
    def testIsCompleteFalse(self):
        self.assertFalse(self.foundationSUT.isComplete())

    def testFitsInFalse(self):
        self.assertFalse(self.foundationSUT.fitsIn(CardBuilder().setSuit(SuitBuilder().setInitial('h').build()).build()))

    def testFitsInTrue(self):
        self.assertTrue(self.foundationSUT.fitsIn(CardBuilder().build()))

    def testGetSuit(self):
        self.assertEqual(self.foundationSUT.getSuit(), SuitBuilder().build())
