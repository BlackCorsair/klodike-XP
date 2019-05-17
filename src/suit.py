from enum import Enum


class Suit(Enum):
    HEARTS = 'h'
    DIAMONDS = 'd'
    CLOVERS = 'c'
    PIKES = 'p'

    def getColor(self):
        return self.color

    @staticmethod
    def find(char):
        if char.lower() == 'h':
            return Suit.HEARTS
        elif char.lower() == 'd':
            return Suit.DIAMONDS
        elif char.lower() == 'c':
            return Suit.CLOVERS
        elif char.lower() == 'p':
            return Suit.PIKES
        else:
            return None

    @staticmethod
    def initials():
        return ['h', 'd', 'c', 'p']


# Aditional attributes
Suit.color = None
