from cardStack import CardStack


class Stock(CardStack):
    def __init__(self):
        CardStack().__init__()

    def takeTop(self, quantity):
        cards = []
        while(not self.empty()):
            cards.insert(self.pop())
