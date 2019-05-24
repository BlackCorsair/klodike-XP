from klondike.suit import Suit
from klondike.number import Number
from klondike.color import Color
from klondike.card import Card


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
