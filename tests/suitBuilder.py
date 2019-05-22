from color import Color
from suit import Suit


class SuitBuilder():
    def __init__(self):
        self.color = Color.BLACK
        self.initial = 'c'

    def setColor(self, color):
        self.color = color
        return self

    def setInitial(self, initial):
        self.initial = initial
        return self

    def build(self):
        s = Suit.find(self.initial)
        s.color = self.color
        return s
