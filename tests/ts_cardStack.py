import unittest
from cardBuilder import CardBuilder
from cardStackBuilder import CardStackBuilder


class TestCardStack(unittest.TestCase):
    def setUp(self):
        self.stack = CardStackBuilder().build()

    def tearDown(self):
        self.stack = None

    def testIsEmptyIsTrue(self):
        self.assertTrue(self.stack.empty())

    def testIsEmptyIsFalse(self):
        self.assertFalse(CardStackBuilder().addNCards(1).build().empty())

    def testPeekWhenEmpty(self):
        self.assertIsNone(self.stack.peek())

    def testPeekWhenNotEmpty(self):
        self.assertEqual(type(CardBuilder().setFaceUp().build()), type(
            CardStackBuilder().addNCards(1).build().peek()))

    def testPopWhenEmpty(self):
        self.assertIsNone(self.stack.pop())

    def testPopWhenNotEmpty(self):
        self.assertEqual(type(CardBuilder().setFaceUp().build()),
                         type(CardStackBuilder().addNCards(1).build().pop()))

    def testPushWhenEmpty(self):
        self.stack.push(CardBuilder().build())
        self.assertEqual(type(CardBuilder().setFaceUp().build()),
                         type(self.stack.pop()))
