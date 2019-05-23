from enum import Enum


class Error(Enum):
    EMPTY_STOCK = "EMPTY_STOCK"
    EMPTY_WASTE = "EMPTY_WASTE"
    EMPTY_FOUNDATION = "EMPTY_FOUNDATION"
    EMPTY_FILE = "EMPTY_FILE"
    NO_EMPTY_STOCK = "NO_EMPTY_STOCK"
    NO_FIT_FOUNDATION = "NO_FIT_FOUNDATION"
    NO_FIT_PILE = "NO_FIT_PILE"
    SAME_PILE = "SAME_PILE"
    NO_ENOUGH_CARDS_PILE = "NO_ENOUGH_CARDS_PILE"

    def __init__(self, message):
        for error in errors:
            if error.value == message:
                message = error.value

    def getMessage(self):
        return message


message = ""
errors = [Error.EMPTY_STOCK, Error.EMPTY_WASTE,
          Error.EMPTY_FOUNDATION, Error.EMPTY_FILE, Error.NO_EMPTY_STOCK,
          Error.NO_EMPTY_STOCK, Error.NO_FIT_FOUNDATION, Error.NO_FIT_PILE,
          Error.SAME_PILE, Error.NO_ENOUGH_CARDS_PILE]
