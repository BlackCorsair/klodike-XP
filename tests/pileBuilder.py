from pile import Pile
from cardBuilder import CardBuilder


class PileBuilder():
    def __init__(self):
        self.number = 2
        self.numberOfFacedUpCards = 1
        self.cards = []

    def setFacedUpCards(self, n):
        self.numberOfFacedUpCards = n
        for i in range(0, self.numberOfFacedUpCards):
            self.cards.append(CardBuilder().setFaceUp().build())
        return self

    def setNumber(self, n):
        self.number = n
        for i in range(0, self.number):
            self.cards.append(CardBuilder().build())
        return self

    def build(self):
        self.setNumber(self.number)
        self.setFacedUpCards(self.numberOfFacedUpCards)
        return Pile(self.number, self.cards)
