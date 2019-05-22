
class Card():
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.facedUp = False

    def flip(self):
        if self.facedUp:
            self.facedUp = False
        else:
            self.facedUp = True
        return self

    def isFacedUp(self):
        return self.facedUp

    def isNextToCard(self, card):
        if type(card) is not type(self):
            return None
        diff = 0
        if self.number.value < card.number.value:
            diff = card.number.value - self.number.value
        else:
            diff = self.number.value - card.number.value

        if diff > 1:
            return False
        else:
            return True

    def getColor(self):
        return self.suit.getColor()

    def getSuit(self):
        return self.suit
