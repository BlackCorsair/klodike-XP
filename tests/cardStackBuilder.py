from cardBuilder import CardBuilder
from klondike.cardStack import CardStack


class CardStackBuilder():
    def __init__(self):
        self.cards = []

    def addCards(self, card):
        self.cards.append(card)
        return self

    def addNCards(self, N):
        for n in range(0, N):
            self.cards.append(CardBuilder().build())
        return self

    def build(self):
        stackie = CardStack()
        if len(self.cards) != 0:
            for card in self.cards:
                stackie.push(card)
        return stackie
