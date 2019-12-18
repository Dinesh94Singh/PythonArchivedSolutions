import enum
import abc


class Card(abc.ABC):
    pass


class Suit(enum.Enum):
    CLUB = enum.auto()
    DIAMOND = enum.auto()

    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value
