from cardStack import CardStack


class Foundation(CardStack):
    def __init__(self, suit):
        self.suit = suit
        super().__init__()

    def isComplete(self):
        if self.empty():
            return False
        if self.peek().getNumber().value != 1:
            return False
        return True

    def fitsIn(self, card):
        if self.isComplete():
            print("I'm complete!")
            return False
        if card.getSuit() != self.suit:
            return False
        return True

    def getSuit(self):
        return self.suit
