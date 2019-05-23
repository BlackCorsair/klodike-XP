from cardStack import CardStack
from number import Number


class Pile(CardStack):
    def __init__(self, number, cards):
        CardStack().__init__()
        self.number = len(cards)
        self.cards = cards
        self.numberOfFacedUpCards = 0
        for card in cards:
            if card.isFacedUp():
                self.numberOfFacedUpCards += 1

    def fitsIn(self, card):
        if not self.empty() and self.peek().getNumber() == Number.KING:
            return False
        if card.getSuit() != self.cards[0].suit:
            return False
        return True

    def getTop(self, numberOfCards):
        cardsToReturn = []
        for i in range(0, numberOfCards):
            if self.empty():
                break
            cardsToReturn.append(self.pop())
        self.numberOfFacedUpCards -= len(cardsToReturn)
        return cardsToReturn

    def addToTop(self, card):
        if not card.isFacedUp():
            raise Exception("ERROR: Can't add card faced down.")
        if not self.empty() and not self.peek().isFacedUp():
            raise Exception("ERROR: Can't add card when top is faced down.")
        if not self.empty() and not self.peek().isNextToCard(card):
            raise Exception("ERROR: Can't add card that is not next to top.")
        self.push(card)
        self.numberOfFacedUpCards += 1

    def removeTop(self, n):
        if not self.empty():
            for i in range(0, n):
                self.pop()

    def getCards(self):
        return self.cards

    def getNumberOfFacedUpCards(self):
        return self.numberOfFacedUpCards
