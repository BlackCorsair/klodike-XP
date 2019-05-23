from klondike.cardStack import CardStack


class Stock(CardStack):
    def __init__(self):
        super().__init__()

    def takeTop(self, quantity):
        cards = []
        while(not self.empty() and len(cards) != quantity):
            cards.append(self.pop())
        return cards
