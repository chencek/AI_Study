class Card:
    def __init__(self, card_suit, card_number):
        self.suit = card_suit
        self.number = card_number

    def __repr__(self):
        return f'({self.__suit},{self.__number:>2})'
    def __str__(self):
        return f'({self.__suit},{self.__number:>2})'