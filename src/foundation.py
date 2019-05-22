class Foundation():
    def __init__(self, suit):
        self.suit = suit

    def isComplete(self):
        return True

    def fitsIn(self, card):
        print(self.suit)
        print(card.suit)
        if card.getSuit() == self.suit:
            return True
        else:
            return False

    def getSuit(self):
        return self.suit
