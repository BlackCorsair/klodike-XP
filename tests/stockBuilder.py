from stock import Stock
from cardBuilder import CardBuilder


class StockBuilder():
    def __init__(self):
        self.numberOfCards = 40

    def setNumberOfCards(self, n):
        self.numberOfCards = n
        return self

    def build(self):
        s = Stock()
        for i in range(0, self.numberOfCards):
            s.push(CardBuilder().build())
        return s
