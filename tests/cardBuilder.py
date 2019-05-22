from suit import Suit
from number import Number
from color import Color
from card import Card


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
