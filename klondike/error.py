from enum import Enum


class Error(Enum):
    EMPTY_STOCK = ("EMPTY_STOCK")
    EMPTY_WASTE = ("EMPTY_WASTE")
    EMPTY_FOUNDATION = ("EMPTY_FOUNDATION")
    EMPTY_FILE = ("EMPTY_FILE")
    NO_EMPTY_STOCK = ("NO_EMPTY_STOCK")
    NO_FIT_FOUNDATION = ("NO_FIT_FOUNDATION")
    NO_FIT_PILE = ("NO_FIT_PILE")
    SAME_PILE = ("SAME_PILE")
    NO_ENOUGH_CARDS_PILE = ("NO_ENOUGH_CARDS_PILE")

    def __init__(self, message):
        self.message = message

    def getMessage(self):
        return self.message
