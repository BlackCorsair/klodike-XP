from enum import Enum


class Suit(Enum):
    HEARTS = 'h'
    DIAMONDS = 'd'
    CLOVERS = 'c'
    PIKES = 'p'

    def getColor(self):
        return self.color

    @staticmethod
    def initial(char):
        if char.lower() == 'h':
            return Suit.HEARTS
        if char.lower() == 'd':
            return Suit.DIAMONDS
        if char.lower() == 'c':
            return Suit.CLOVERS
        if char.lower() == 'p':
            return Suit.PIKES

    @staticmethod
    def initials():
        return ['h', 'd', 'c', 'p']


# Aditional attributes
Suit.color = None
