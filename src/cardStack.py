class CardStack:
    def __init__(self):
        self.cards = []

    def pop(self):
        if self.empty():
            return None
        cardToReturn = self.cards.pop()
        if not self.empty() and not self.cards[-1].isFacedUp():
            self.cards[-1].flip()
        return cardToReturn

    def push(self, card):
        self.cards.append(card)

    def peek(self):
        if self.empty():
            return None
        else:
            self.cards[-1].flip()
            return self.cards[-1]

    def empty(self):
        if len(self.cards) == 0:
            return True
        else:
            return False
